import datetime
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template import TemplateDoesNotExist

from account.models import Account
from plants.models import PlantEvent

@login_required(login_url='/account/sign-in')
def calendar_home(request):
	all_events = PlantEvent.objects.all()
	# fmt_date = all_events.event_start.strftime("%-m/%d/%y")

	plant_event = {
		'event': all_events,
		# 'fmt_date': fmt_date
	}

	context = {
		'events': plant_event
	}

	if request.user.is_active:
		context['logged_in'] = True
		account = Account.objects.get(logon_credentials=request.user)

		context['user_id'] = account.id
	else:
		return HttpResponseRedirect('/')

	return render(request, 'plant_calendar/calendar.html', context)

def angular_views(request, page_name):

	try:
		return render(request, 'angular/%s' % page_name)
	except TemplateDoesNotExist:
		raise Http404
