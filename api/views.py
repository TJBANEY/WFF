from rest_framework.response import Response
from rest_framework.decorators import detail_route
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
			plant.plantevent_set.all(), many=True)
		return Response(serializer.data)

	@detail_route(methods=['post'])
	def filtered_plants(self, request, pk=None):
		# harvest_start = request.GET['start']
		# harvest_end = request.GET['end']
		name = request.GET['plant_name']
		# type = request.GET['plant_type']

		plants = self.queryset.filter(botanical_name=name)

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
