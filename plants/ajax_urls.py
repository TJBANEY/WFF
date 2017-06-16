from django.conf.urls import url
from .ajax_views import get_plants

urlpatterns = [
	url(r'^get_plants', get_plants, name='get_plants')
]
