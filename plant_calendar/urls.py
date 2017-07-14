from django.conf.urls import url
from .views import calendar_home, angular_views

urlpatterns = [
	url(r'^views/(?P<page_name>[-\w]+.html)/?$', angular_views, name='angular_views'),
	url(r'^$', calendar_home, name='calendar')
]
