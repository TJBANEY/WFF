from django.conf.urls import url
from .views import register, register_plants, register_payment, sign_in

urlpatterns = [
	url(r'^register/payment', register_payment, name='register_payment'),
	url(r'^register/plants', register_plants, name='register_plants'),
	url(r'^register', register, name='register'),
	url(r'^sign-in', sign_in, name='sign_in')
]
