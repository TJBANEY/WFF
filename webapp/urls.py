from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework import routers
from api.views import *

from . import views as webapp_views

admin.site.site_header = 'Site Header'
admin.site.index_title = 'Site Index Title'
admin.site.site_title = 'Site Title'

admin.autodiscover()

router = routers.SimpleRouter()
router.register(r'plants', PlantViewSet),
router.register(r'events', PlantEventViewSet)

urlpatterns = [
	url(r'^$', webapp_views.view_home, name='home'),
	url(r'^account/', include('account.urls')),
	url(r'^plants/', include('plants.ajax_urls')),
	url(r'^calendar/', include('plant_calendar.urls')),
	url(r'^inplaceeditform/', include('inplaceeditform.urls')),
	url(r'^admin/filebrowser/', include('filebrowser.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api-auth/', include('rest_framework.urls',
							   namespace='rest_framework')),
	url(r'^api/v1/', include(router.urls,
							 namespace='apiv1'))
]

if settings.DEVELOPMENT:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# This url pattern must be last since it will match on anything
# urlpatterns += [url(r'^.+/', nav_views.default), ]
