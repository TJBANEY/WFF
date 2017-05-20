import logging

from django.contrib import sitemaps
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def view_home(request):


    context = {}
    template = 'home.html'

    return HttpResponse('This works')

    # return render_to_response(template, context, context_instance=RequestContext(request))


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = 'monthly'

    def items(self):
        return ['home', ]

    def location(self, item):
        return reverse(item)
