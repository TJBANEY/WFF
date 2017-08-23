from django.conf.urls import url
from .views import register, register_plants, register_payment, sign_in, sign_out, my_garden

urlpatterns = [
	url(r'^register/payment', register_payment, name='register_payment'),
	url(r'^register/plants', register_plants, name='register_plants'),
	url(r'^register', register, name='register'),
	url(r'^sign-in', sign_in, name='sign_in'),
	url(r'^sign-out', sign_out, name='sign_out'),
	url(r'^my-garden', my_garden, name='my_garden')
]
