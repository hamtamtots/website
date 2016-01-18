from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='blog_list'),
    url(r'^tagged/(?P<tag>.*)$', TaggedArticleListView.as_view(), name='blog_tagged_list'),
    url(r'^(?P<pk>.*)$', ArticleView.as_view(), name='blog_article'),
]