import datetime
import logging
import os

# import scrapy
import urllib3

from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from plants.models import Plant, PlantImage


def explore_plants(request):
	p_images = PlantImage.objects.all()

	context = {
		'p_images': p_images
	}

	return render(request, 'plants/explore.html', context)

def crawl_plant_images(request):
	all_plants = Plant.objects.all()
	count = 1

	for plant in all_plants:
		if count % 10 == 0:
			print("{} out of {}".format(count, all_plants.count()))

		plant_url = "https://www.google.com/search?q={}".format(plant.scientific_name)
		r = requests.get(plant_url)
		data = r.text
		soup = BeautifulSoup(data, 'html.parser')
		plant_links = soup.findAll("a")
		link_text = [link for link in plant_links if link.get_text().lower() == "images"]

		img_list_url = 'http://www.google.com/{}'.format(link_text[1]['href'])
		r = requests.get(img_list_url)
		data = r.text
		soup = BeautifulSoup(data, 'html.parser')
		plant_images = soup.findAll("img")
		img_src = plant_images[0]['src']

		try:
			PlantImage.objects.get(plant=plant)
		except PlantImage.DoesNotExist:
			print(img_src)
			new_plant_img = PlantImage()

			new_plant_img.plant = plant
			new_plant_img.image_url = img_src

			# To-Do: Understand how this works
			img_temp = NamedTemporaryFile(delete=True)
			img_temp.write(requests.get(img_src).content)
			img_temp.flush()
			new_plant_img.image.save(os.path.basename(img_src), File(img_temp))

			new_plant_img.save()

		count += 1

	return HttpResponse("Works!")

def crawl_usda(request):
	print(datetime.datetime.now())
	usda_url = "https://plants.usda.gov/java/stateSearch"
	r = requests.get(usda_url)
	data = r.text

	soup = BeautifulSoup(data, 'html.parser')
	all_rows = soup.findAll("tr", {"class": "rowon"})

	row_length = len(list(all_rows))

	for x in range(0, row_length):
		if len(list(all_rows[x].findChildren("td"))) > 1:  # If the row has two td's

			sci_block = list(all_rows[x].findChildren("td"))[0].findChildren("a")
			if len(sci_block) > 0:  # If the scientific name has an anchor tag in it
				sci_name = sci_block[0].get_text()  # Get the entire scientific name, em's and all

			common_name = all_rows[x].findChildren("td")[1].get_text()
			usda_code = all_rows[x].findChildren("th")
			if len(usda_code) > 0:
				code = usda_code[0].get_text()

			# If there is a scientific name, and a common name
			if common_name != '' and len(sci_name) > 0:
				try:
					Plant.objects.create(scientific_name=sci_name, botanical_name=common_name, usda_code=code)
				except Exception as e:
					pass

	print(datetime.datetime.now())

	data_length = Plant.objects.all().count()

	return HttpResponse('Works There Were 0 Plants, Now There are {}'.format(data_length))

def crawl_characteristics(request):
	all_plants = Plant.objects.all()

	for plant in all_plants[:1]:
		plant_url = "https://plants.usda.gov/java/charProfile?symbol=ABGR4"
		r = requests.get(plant_url)
		html = r.text
		page = BeautifulSoup(html, 'html.parser')

		try:
			chr_table = page.table.findAll("table")[1].findAll("table")[2].findAll("table")
			table_one = chr_table[1].findAll("tr")

			# Begin extracting characteristics
			flower_color = table_one[8].findAll("td")[1].get_text()
			foliage_color = table_one[10].findAll("td")[1].get_text()

			plant.flower_color = flower_color
			plant.foliage_color = foliage_color

			print(flower_color)
			print(foliage_color)
		except Exception as e:
			print(e)
			# print('No page found for .'.format(plant.usda_code))
			pass

	return HttpResponse('Done')

def clean_up_genus_species():
	plants = Plant.objects.all()

	count = 1
	for plant in plants:
		genus = plant.scientific_name.split()[0].capitalize()

		if len(plant.scientific_name.split()) > 1:
			split_species = list(plant.scientific_name.split()[1])

			# Check for weird miniature x, or period by check ASCII value
			prohibited = [46, 215]
			for char in split_species:
				if ord(char) in prohibited:
					split_species.remove(char)
				if ord(char) in [41, 40]:
					split_species = [""]
					break

			species = "".join(split_species).capitalize()
			if len(species) <= 2:
				species = ""
		else:
			species = ""

		plant.scientific_name = '{} {}'.format(genus, species)
		plant.save()
		print('{} out of {} complete'.format(count, plants.count()))
		count += 1

def growth_habit_crawl(request):
	# Data will be drawn from the "Encyclopedia of life" website
	# double check for permissions, and make a donation.

	# Error Occuring at about 320, don't forget about "320 - 600"
	for plant in Plant.objects.filter(growth_habit="NA").order_by("-scientific_name")[600:]:
		print("----------------------------")
		search_compatible_name = plant.scientific_name.replace(" ", "+")
		plant_url = "http://eol.org/search?q={}&search=Go".format(search_compatible_name)
		r = requests.get(plant_url)
		html = r.text
		print("Crawling for {} at url {}".format(plant.scientific_name, plant_url))

		try:
			page = BeautifulSoup(html, 'html.parser')

			search_page = False

			headers = page.findAll("h1")
			for item in headers:
				if item.get_text().lower() == "search results":
					search_page = True
					break

			if search_page:
				results = page.find("div", {"class": "filtered_search"}).find("ul")
				plant_url = results.findAll("li", {"class": "taxon"})[0].findAll("a")[0]["href"]

				print("Hit Search Page")
				plant_url = "http://eol.org{}".format(plant_url)
				print("Crawling {}".format(plant_url))

				r = requests.get(plant_url)
				html = r.text
				page = BeautifulSoup(html, 'html.parser')

			data_box = page.find("div", {"class": "data_div"})
			data_fields = data_box.findAll("span")

			for field in data_fields:

				# Get Plant Type
				if field.get_text().lower().replace("\n", "") == "growth habit":
					print("Growth Field Found")

					growth_field = field.parent.find_next_siblings("td")[1]
					growth_list = [item for item in growth_field.childGenerator()]

					growth_type = growth_list[0].replace("\n", "")

					print(growth_type)

					plant.growth_habit = growth_type

					print("Success, Growth Type for {} Saved".format(plant.scientific_name))

				# Get Plant Life Span
				if field.get_text().lower().replace("\n", "") == "life cycle habit":
					print("Life Cycle Found")

					cycle_field = field.parent.find_next_siblings("td")[1]
					cycle_list = [item for item in cycle_field.childGenerator()]

					cycle_type_one = cycle_list[0].replace("\n", "")

					if cycle_type_one == "annual":
						plant.annual = True
					elif cycle_type_one == "perennial":
						plant.perennial = True
					elif cycle_type_one == "biennial":
						plant.biennial = True

					if len(cycle_list) > 1:

						cycle_type_two = cycle_list[1].get_text().replace("\n", "")

						if cycle_type_two == "annual":
							plant.annual = True
						elif cycle_type_two == "perennial":
							plant.perennial = True
						elif cycle_type_two == "biennial":
							plant.biennial = True

					print(cycle_type_one)
					print("Success, Life Cycle for {} Saved".format(plant.scientific_name))
					print("--------------------------\n")

				plant.save()

		except Exception as e:
			print("Something went wrong, moving on ...")
			print(e)
			print("--------------------------------\n")
			pass

	return HttpResponse("Done")
