import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from plants.models import Plant


@csrf_exempt
def get_plants(request):
	all_plants = Plant.objects.all()

	json_data = {

	}

	return HttpResponse(json.dumps(json_data), content_type='application/json')
