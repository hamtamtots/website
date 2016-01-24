from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', TagListView.as_view(), name='blog_list'),
    url(r'^tagged/(?P<tag>.*)$', TaggedArticleListView.as_view(), name='blog_tagged_list'),
    url(r'^(?P<key>.*)$', ArticleView.as_view(), name='blog_article'),
]