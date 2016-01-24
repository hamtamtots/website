from django.db import models
from .tag import Tag
from .articlebody import ArticleBody

class Article(models.Model):

    id = models.AutoField(primary_key = True)
    key = models.CharField(max_length = 1000)
    title = models.CharField(max_length = 1000)
    tags = models.ManyToManyField(Tag, related_name='articles')
    created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    body = models.OneToOneField(ArticleBody)

    def __str__(self):
        return self.title