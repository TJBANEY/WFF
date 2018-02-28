from django.conf.urls import url
from .views import calendar_home, angular_views, navigate_months

urlpatterns = [
    # url(r'^views/(?P<page_name>[-\w]+.html)/?$', angular_views, name='angular_views'),
    url(r'^navigate/(?P<direction>.*)/?$', navigate_months, name='navigate_months'),
    url(r'^(?P<plant>.*)/?$', calendar_home, name='calendar'),
    url(r'^$', calendar_home, name='calendar')
    # url(r'^$', info, name='info'),
]
