from django.db import models
from .tag import Tag

class Article(models.Model):

    key = models.CharField(max_length = 1000, primary_key = True)
    title = models.CharField(max_length = 1000)
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    body = models.TextField()

    def __str__(self):
        return self.title