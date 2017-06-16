import json

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

from plants.models import Plant


@csrf_exempt
def get_plants(request):
	body_unicode = request.body.decode('utf-8')
	value = body_unicode.split('=')[1]

	plants = Plant.objects.filter(botanical_name__icontains=value)

	results = render_to_string('plants/ajax/plant_results.html', {'plants': plants})

	json_data = {
		'results': results
	}

	return HttpResponse(json.dumps(json_data), content_type='application/json')
