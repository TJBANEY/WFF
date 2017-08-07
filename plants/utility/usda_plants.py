# Web scraping for USDA site to fill in PostgreSQL database

from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests

def crawl_usda(request):

	usda_url = "https://plants.usda.gov/java/stateSearch"
	r = requests.get(usda_url)
	data = r.text

	soup = BeautifulSoup(data)

	return HttpResponse(soup)


	# all_messages = soup.findAll("div", {"class": "message"})
	# msg_dictionaries = [{
	# 						'user': el.findAll('span')[0],
	# 						'time': el.findAll('span')[1],
	# 						'content': el.nextSibling.nextSibling
	# 					} for el in all_messages]
	#
	# for msg in msg_dictionaries[0:5]:
	# 	print(msg['user'])
	# 	fbuser = FacebookUser.objects.create(full_name=msg['user'])
	#
	# 	new_msg = Message()
	#
	# 	new_msg.content = msg['content']
	# 	new_msg.user = fbuser
	# 	new_msg.save()
	#
	# return HttpResponse('Worked ! Check the Admin')