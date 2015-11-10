from django.conf.urls import url

from link.views.linkview import LinkView

urlpatterns = [
    url(r'^(?P<key>.*)$', LinkView.as_view(), name='link'),
]