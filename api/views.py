import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from account.models import Account
from rest_framework.renderers import JSONRenderer

# from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework import mixins

from rest_framework import generics

from plants.models import Plant, PlantEvent, UserPlant
from .serializers import PlantSerializer, PlantEventSerializer, UserSerializer

from rest_framework import viewsets


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

class UserViewSet(viewsets.ModelViewSet):
	queryset = Account.objects.all()
	serializer_class = UserSerializer

	@detail_route(methods=['get'])
	def events(self, request, pk=None):
		user = self.get_object()

		user_plants = UserPlant.objects.filter(user=user).values_list('plant', flat=True)

		serializer = PlantEventSerializer(
			PlantEvent.objects.filter(plant__id__in=user_plants), many=True
		)
		return Response(serializer.data)
