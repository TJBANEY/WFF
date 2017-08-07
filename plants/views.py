import datetime

from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests

from plants.models import Plant


def explore_plants(request):
	context = {}

	return render(request, 'plants/explore.html', context)


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
