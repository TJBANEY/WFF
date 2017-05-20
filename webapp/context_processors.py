import logging
from django.contrib.sites.models import Site

def detail_context(request):

    # AJAX requests will almost never need this context data, so avoid the extra processing
    if request.is_ajax():
        return {}

    a_context = {}

    # CHECK FOR ADMIN USER
    active_user = None
    try:
        if request.user.is_superuser:
            active_user = request.user
    except Exception as e:
        logging.error(e)

    a_context['active_user'] = active_user

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
