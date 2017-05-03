import logging

from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

from home_content.models import HomeSection, Billboard, MiniBillboard


def view_home(request):
    try:
        sections = HomeSection.get_published_objects()
    except Exception as e:
        logging.error(e)
        sections = None

    try:
        billboards = Billboard.get_published_objects()
    except Exception as e:
        logging.error(e)
        billboards = None

    try:
        mini_billboards = MiniBillboard.get_published_objects()
    except Exception as e:
        logging.error(e)
        mini_billboards = None

    context = {'sections': sections, 'billboards': billboards, 'mini_billboards': mini_billboards}
    template = 'home.html'

    return render_to_response(template, context, context_instance=RequestContext(request))


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = 'monthly'

    def items(self):
        return ['home', ]

    def location(self, item):
        return reverse(item)
