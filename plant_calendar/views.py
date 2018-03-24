import datetime
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

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

    # all_events = PlantEvent.objects.filter(plant=target_plant)
    #
    # json_events = json.dumps([{
    #     'title': event.name,
    #     'start': datetime.datetime.strftime(event.event_start, '%Y-%m-%d'),
    #     'end': datetime.datetime.strftime(event.event_end, '%Y-%m-%d')
    # } for event in all_events])

    months = {
        '1': 'january',
        '2': 'february',
        '3': 'march',
        '4': 'april',
        '5': 'may',
        '6': 'june',
        '7': 'july',
        '8': 'august',
        '9': 'september',
        '10': 'october',
        '11': 'november',
        '12': 'december'
    }

    if request.session.get('curr_day'):
        del request.session['curr_day']

    now = datetime.datetime.now()
    curr_month_num = request.session['curr_month_num'] if 'curr_month_num' in request.session else int(
        now.strftime('%-m'))
    curr_year = request.session['curr_year'] if 'curr_year' in request.session else now.year

    request.session['curr_month_num'] = curr_month_num
    request.session.modified = True

    month = months[str(curr_month_num)]

    year = curr_year

    context = {
        'month': month,
        'year': year,
        'request': request,
        'curr_month_num': request.session['curr_month_num'],
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

@csrf_exempt
def navigate_months(request, direction):
    months = {
        '1': 'january',
        '2': 'february',
        '3': 'march',
        '4': 'april',
        '5': 'may',
        '6': 'june',
        '7': 'july',
        '8': 'august',
        '9': 'september',
        '10': 'october',
        '11': 'november',
        '12': 'december'
    }

    del request.session['curr_day']

    now = datetime.datetime.now()
    curr_month_num = request.session['curr_month_num'] if 'curr_month_num' in request.session else int(now.strftime('%-m'))
    curr_month_name = request.session['curr_month_name'] if 'curr_month_name' in request.session else now.strftime('%B').lower()

    curr_year = request.session['curr_year'] if 'curr_year' in request.session else now.year

    if direction == 'next':
        if curr_month_name == 'december':
            next_year = curr_year + 1
            next_month = 'January'
            request.session['curr_month_num'] = 1
        else:
            next_month = months[str(curr_month_num + 1)]
            next_year = curr_year
            request.session['curr_month_num'] = curr_month_num + 1

        request.session['curr_month_name'] = next_month
        request.session['curr_year'] = next_year

        context = {
            'month': next_month,
            'year': next_year,
            'request': request,
            'curr_month_num': request.session['curr_month_num'],
        }

    else:
        if curr_month_name == 'january':
            prev_year = curr_year - 1
            prev_month = 'December'
            request.session['curr_month_num'] = 12
        else:
            prev_month = months[str(curr_month_num - 1)]
            prev_year = curr_year
            request.session['curr_month_num'] = curr_month_num - 1

        request.session['curr_month_name'] = prev_month
        request.session['curr_year'] = prev_year

        context = {
            'month': prev_month,
            'year': prev_year,
            'request': request,
            'curr_month_num': request.session['curr_month_num'],
        }

    template = json.dumps(render_to_string('plant_calendar/calendar_month.html', context))

    request.modified = True

    return HttpResponse(template, content_type='application/json')