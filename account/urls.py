from django.conf.urls import url
from .views import register, register_plants

urlpatterns = [
	url(r'^register/plants', register_plants, name='register_plants'),
	url(r'^register', register, name='register'),
]
