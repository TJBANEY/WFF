# import datetime

from dateutil import parser
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets

from plants.models import Plant, PlantEvent, UserPlant
from account.models import Account

from .serializers import PlantSerializer, PlantEventSerializer, UserSerializer, UserPlantSerializer


class PlantViewSet(viewsets.ModelViewSet):
	queryset = Plant.objects.all()
	serializer_class = PlantSerializer

	@detail_route(methods=['get'])
	def events(self, request, pk=None):
		plant = self.get_object()
		serializer = PlantEventSerializer(
			plant.events.all(), many=True)
		return Response(serializer.data)


	@list_route()
	def filtered_plants(self, request):
		harvest_start = request.query_params.get('harvest_start', None)
		harvest_start = parser.parse(harvest_start)

		harvest_end = request.query_params.get('harvest_end', None)

		name = request.query_params['name']
		type = request.query_params.get('plant_type', None)

		plants = self.queryset.all()
		if harvest_start:
			plants = plants.filter(harvest_time_start__gte=harvest_start)
		if harvest_end:
			plants = plants.filter(harvest_time_end__lte=harvest_end)
		if name:
			plants = plants.filter(botanical_name__icontains=name)
		if type:
			plants = plants.filter(plant_type=type)

		serializer = PlantSerializer(plants, many=True)
		return Response(serializer.data)

class PlantEventViewSet(viewsets.ModelViewSet):
	queryset = PlantEvent.objects.all()
	serializer_class = PlantEventSerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = Account.objects.all()
	serializer_class = UserSerializer

	@detail_route(methods=['get'])
	def events(self, request, pk=None):
		user = self.get_object()

		user_plants = UserPlant.objects.filter(user=user).values_list('plant', flat=True)

		serializer = PlantEventSerializer(
			PlantEvent.objects.filter(plant__id__in=user_plants)
		)
		return Response(serializer.data)


class UserPlantViewSet(viewsets.ModelViewSet):
	queryset = UserPlant.objects.all()
	serializer_class = UserPlantSerializer
