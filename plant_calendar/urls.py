from django.conf.urls import url
from .views import calendar

urlpatterns = [
	url(r'^$', calendar, name='calendar')
]
