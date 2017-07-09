from django.conf.urls import url
from .views import calendar_home

urlpatterns = [
	url(r'^$', calendar_home, name='calendar')
]
