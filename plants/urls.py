from django.conf.urls import url
from .views import explore_plants, crawl_plant_images, plant_info

urlpatterns = [
	url(r'^explore', explore_plants, name='explore_plants'),
	url(r'^(?P<plant_slug>.*)/?$', plant_info, name='plant_info')
]
