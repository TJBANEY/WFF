import datetime

from django.shortcuts import render

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
