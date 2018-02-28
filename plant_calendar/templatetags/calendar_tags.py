import datetime
from django import template

register = template.Library()

@register.simple_tag
def has_user_plant(day, plant):
    x = plant

    if 'curr_month_num' in plant:
        return plant.session['curr_month_num']
    else:
        return 'Nope'

@register.simple_tag
def first_day_of_month(weekday, request, *args, **kwargs):
    now = datetime.datetime.now()

    curr_month_num = request.session['curr_month_num'] if 'curr_month_num' in request.session else int(now.strftime('%-m'))
    curr_year = request.session['curr_year'] if 'curr_year' in request.session else now.year
    curr_day = request.session['curr_day'] + 1 if 'curr_day' in request.session else 1

    current_calendar_month = datetime.datetime.strptime("{}/{}/{}".format(curr_month_num, curr_day, curr_year),"%m/%d/%Y")
    day_1_weekday = current_calendar_month.weekday()

    if day_1_weekday == weekday:
        request.session['curr_day'] = curr_day
        request.modified = True

        return '<div class="day-triangle"></div><p class="day">' + str(curr_day) + '</p>'
    else:
        return ''