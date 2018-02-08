import datetime
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template import TemplateDoesNotExist

from account.models import Account
from plants.models import PlantEvent, UserPlant, Plant


@login_required(login_url='/account/sign-in')
def calendar_home(request, plant):
	account = Account.current_user(request)
	if plant:
		plant = plant.rstrip('/')

	# Get all plant events for the plants belonging to the user
	account_plants = UserPlant.objects.filter(user=account)
	acct_plant_flatlist = account_plants.values_list('plant', flat=True)

	if plant:
		try:
			plant = Plant.objects.get(slug=plant)

			if plant.id in acct_plant_flatlist:
				target_plant = plant
			else:
				raise Http404

		except Plant.DoesNotExist:
			raise Http404
	else:
		if account_plants:
			target_plant = account_plants[0].plant
		else:
			target_plant = None

	all_events = PlantEvent.objects.filter(plant=target_plant)

	json_events = json.dumps([{
								  'title': event.name,
								  'start': datetime.datetime.strftime(event.event_start, '%Y-%m-%d'),
								  'end': datetime.datetime.strftime(event.event_end, '%Y-%m-%d')
							  } for event in all_events])

	# Format the QuerySet into json that FullCalendar.js can recognize

	# fmt_date = all_events.event_start.strftime("%-m/%d/%y")

	context = {
		'events': json_events,
		'account_plants': account_plants
	}

	return render(request, 'plant_calendar/calendar.html', context)



# @login_required(login_url='/account/sign-in')
# def info(request, plant):
# 	account = Account.current_user(request)
# 	if plant:
# 		plant = plant.rstrip('/')

# 	# Get all plant events for the plants belonging to the user
# 	account_plants = UserPlant.objects.filter(user=account)
# 	acct_plant_flatlist = account_plants.values_list('plant', flat=True)

# 	if plant:
# 		try:
# 			plant = Plant.objects.get(slug=plant)

# 			if plant.id in acct_plant_flatlist:
# 				target_plant = plant
# 			else:
# 				raise Http404

# 		except Plant.DoesNotExist:
# 			raise Http404
# 	else:
# 		if account_plants:
# 			target_plant = account_plants[0].plant
# 		else:
# 			target_plant = None

# 	all_events = PlantEvent.objects.filter(plant=target_plant)

# 	json_events = json.dumps([{
# 								  'title': event.name,
# 								  'start': datetime.datetime.strftime(event.event_start, '%Y-%m-%d'),
# 								  'end': datetime.datetime.strftime(event.event_end, '%Y-%m-%d')
# 							  } for event in all_events])

# 	# Format the QuerySet into json that FullCalendar.js can recognize

# 	# fmt_date = all_events.event_start.strftime("%-m/%d/%y")

# 	context = {
# 		'events': json_events,
# 		'account_plants': account_plants
# 	}

# 	return render(request, 'plant_calendar/info.html', context)


def angular_views(request, page_name):
	try:
		return render(request, 'angular/%s' % page_name)
	except TemplateDoesNotExist:
		raise Http404
