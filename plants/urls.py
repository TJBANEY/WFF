from django.conf.urls import url
from .views import explore_plants

urlpatterns = [
	url(r'^explore', explore_plants, name='explore_plants')
]