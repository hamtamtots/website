from django.views.generic import RedirectView
from django.shortcuts import get_object_or_404

from link.models.link import Link

class LinkView(RedirectView):
    
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        link = get_object_or_404(Link, key=kwargs['key'])
        return link.url