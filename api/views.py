import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from rest_framework.renderers import JSONRenderer

# from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework import mixins

from rest_framework import generics

from plants.models import Plant, PlantEvent
from .serializers import PlantSerializer, PlantEventSerializer

from rest_framework import viewsets


# class ListCreatePlant(APIView):
# 	def get(self, request, format=None):
# 		plants = Plant.objects.all()
# 		serializer = PlantSerializer(plants, many=True)
#
# 		return Response(serializer.data)
#
# 	def post(self, request, format=None):
# 		serializer = PlantSerializer(data=request.data)
# 		serializer.is_valid(raise_exception=True)
# 		serializer.save()
# 		return Response(serializer.data, status=status.HTTP_201_CREATED)

# ================================================================ #
# ================================================================ #

class ListCreatePlant(generics.ListCreateAPIView):
	queryset = Plant.objects.all()
	serializer_class = PlantSerializer


class RetrieveUpdateDestroyPlant(generics.RetrieveUpdateDestroyAPIView):
	queryset = Plant.objects.all()
	serializer_class = PlantSerializer


class ListCreatePlantEvent(generics.ListCreateAPIView):
	queryset = PlantEvent.objects.all()
	serializer_class = PlantEventSerializer

	def get_queryset(self):
		return self.queryset.filter(plant=self.kwargs.get('plant_id'))

	def perform_create(self, serializer):
		event = get_object_or_404(PlantEvent, id=self.kwargs.get('event_id'))
		serializer.save(PlantEvent=event)


class RetrieveUpdateDestroyPlantEvent(generics.RetrieveUpdateDestroyAPIView):
	queryset = PlantEvent.objects.all()
	serializer_class = PlantEventSerializer

	def get_object(self):
		return get_object_or_404(self.get_queryset(),
								 plant=self.kwargs.get('plant_id'),
								 id=self.kwargs.get('event_id'))

# ===================================================================== #
# ===================================================================== #

class PlantViewSet(viewsets.ModelViewSet):
	queryset = Plant.objects.all()
	serializer_class = PlantSerializer

	@detail_route(methods=['get'])
	def events(self, request, pk=None):
		plant = self.get_object()
		serializer = PlantEventSerializer(
			plant.plantevent_set.all(), many=True)
		return Response(serializer.data)


class PlantEventViewSet(viewsets.ModelViewSet):
	queryset = PlantEvent.objects.all()
	serializer_class = PlantEventSerializer
