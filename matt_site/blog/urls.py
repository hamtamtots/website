from django.conf.urls import url

from blog.views import *

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='blog_list'),
    url(r'^tags/$', TagListView.as_view(), name='blog_tag_list'),
    url(r'^tag/(?P<tag>.*)$', TaggedArticleListView.as_view(), name='blog_tagged_list'),
    url(r'^(?P<key>.*)$', ArticleView.as_view(), name='blog_article'),
]