from django.contrib import admin

from blog.models.article import Article
from blog.models.articlebody import ArticleBody
from blog.models.tag import Tag

admin.site.register(Article)
admin.site.register(ArticleBody)
admin.site.register(Tag)