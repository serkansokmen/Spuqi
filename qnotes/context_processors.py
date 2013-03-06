from django.contrib.sites.models import Site
from apps.quotes.models import Quote


def site_processor(request):
    return {
        'site': Site.objects.get_current(),
        'PRIVACY_STATES': Quote.PRIVACY_STATES
    }
