from django.conf.urls import url
from .views import ListCreatePlant, RetrieveUpdateDestroyPlant, ListCreatePlantEvent, RetrieveUpdateDestroyPlantEvent

urlpatterns = [
	url(r'^$', ListCreatePlant.as_view(), name='plant_list'),
	url(r'^(?P<pk>\d+)/$', RetrieveUpdateDestroyPlant.as_view(), name='update_plants'),
	url(r'^(?P<plant_id>\d+)/events/$', ListCreatePlantEvent.as_view(), name='update_plants'),
	url(r'^(?P<plant_id>\d+)/events/(?P<event_id>\d+)$', RetrieveUpdateDestroyPlantEvent.as_view(), name='update_plants')
]
