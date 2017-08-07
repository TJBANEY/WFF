from django.conf.urls import url
from .views import explore_plants, crawl_usda

urlpatterns = [
	url(r'^explore', crawl_usda, name='explore_plants')
]