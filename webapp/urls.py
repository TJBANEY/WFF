from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from navigation import views as nav_views
from navigation.navSiteMap import NavSitemap
from page_content.page_site_map import PageSiteMap
from webapp.views import StaticViewSitemap
from . import views as webapp_views

admin.site.site_header = 'Site Header'
admin.site.index_title = 'Site Index Title'
admin.site.site_title = 'Site Title'

site_maps = {
    'static': StaticViewSitemap,
    'navigation': NavSitemap,
    'pages': PageSiteMap,
}

admin.autodiscover()

urlpatterns = [
    url(r'^$', webapp_views.view_home, name='home'),
    url(r'^inplaceeditform/', include('inplaceeditform.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': site_maps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^admin/filebrowser/', include('filebrowser.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEVELOPMENT:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# This url pattern must be last since it will match on anything
urlpatterns += [url(r'^.+/', nav_views.default), ]
