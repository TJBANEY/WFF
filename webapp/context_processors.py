import logging
from django.contrib.sites.models import Site

def detail_context(request):
    a_context = {}

    # CHECK FOR ADMIN USER
    if request.user.is_active:
        a_context['user'] = request.user
    else:
        a_context['user'] = None

    # NAV LINKS
    # desktop_links = PrimaryNavigation.get_published_objects()
    # a_context['desktop_links'] = desktop_links

    # nav_links = PrimaryNavigation.get_published_objects()
    # a_context['nav_links'] = nav_links

    try:
        # GET CURRENT SITE
        current_site = Site.objects.get_current()
        a_context['current_site'] = current_site

    except Exception as e:
        logging.error(e)
        current_site = None

    return a_context
