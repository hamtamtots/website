from django.db import models

class ArticleBody(models.Model):

    id = models.AutoField(primary_key = True)
    body = models.TextField()