"""
Definition of urls for matt_site.
"""

from django.conf.urls import patterns, url
from django.conf.urls import include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^$', include('home.urls')),
    url(r'^links/', include('link.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
