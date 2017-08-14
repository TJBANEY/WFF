from django.conf.urls import url
from .views import explore_plants, crawl_usda, crawl_plant_images, crawl_characteristics, growth_habit_crawl

urlpatterns = [
	url(r'^explore', growth_habit_crawl, name='explore_plants')
]
