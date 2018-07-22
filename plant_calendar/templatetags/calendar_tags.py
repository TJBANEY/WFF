import datetime
from django import template

from plants.models import PlantEvent

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
    first = kwargs.get('first', '')

    curr_month_num = request.session['curr_month_num'] if 'curr_month_num' in request.session else int(
        now.strftime('%-m'))
    curr_year = request.session['curr_year'] if 'curr_year' in request.session else now.year
    curr_day = request.session['curr_day'] + 1 if 'curr_day' in request.session else 1

    try:
        current_calendar_month = datetime.datetime.strptime("{}/{}/{}".format(curr_month_num, curr_day, curr_year),
                                                            "%m/%d/%Y")
    except Exception as e:
        return '''<div class="column {}">
                </div>
            '''.format(first)

    day_1_weekday = current_calendar_month.weekday()

    if day_1_weekday == weekday:
        request.session['curr_day'] = curr_day
        request.modified = True
        event_start = curr_day - 1
        plant_events = PlantEvent.objects.filter(event_start__day=event_start, event_start__month=curr_month_num).first()

        if plant_events is not None:
            return '''<div class="column {}">
                        <div class="day"></div>
                        <p class="day">{}</p>
                        <div class='event' style='background: #{}; color: #{}'>{}</div>
                    </div>
            '''.format(first, str(curr_day), plant_events.color, plant_events.text_color, str(plant_events.name))
        else:
            return '''<div class="column {}"> 
                        <p class="day active">{}</p>
                    </div>
            '''.format(first, str(curr_day))
    else:
        return '''<div class="column {}">
                </div>
            '''.format(first)
