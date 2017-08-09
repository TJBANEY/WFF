from django.conf.urls import url
from .views import explore_plants, crawl_usda, crawl_plant_images

urlpatterns = [
	url(r'^explore', explore_plants, name='explore_plants')
]
