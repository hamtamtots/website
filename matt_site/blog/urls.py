from django.conf.urls import url

from .views.articleview import ArticleView

urlpatterns = [
    url(r'^(?P<pk>.*)$', ArticleView.as_view(), name='blog_article'),
]