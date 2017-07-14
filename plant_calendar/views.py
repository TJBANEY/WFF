import datetime
import json

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist

from plants.models import PlantEvent


def calendar_home(request):
	all_events = PlantEvent.objects.all()[0]
	fmt_date = all_events.event_start.strftime("%-m/%d/%y")

	plant_event = {
		'event': all_events,
		'fmt_date': fmt_date
	}

	context = {
		'events': plant_event
	}

	return render(request, 'plant_calendar/calendar.html', context)

def angular_views(request, page_name):

	try:
		return render(request, 'angular/%s' % page_name)
	except TemplateDoesNotExist:
		raise Http404
