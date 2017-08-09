import datetime
import os

import scrapy
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
