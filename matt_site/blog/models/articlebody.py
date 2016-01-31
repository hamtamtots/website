from django.db import models

class ArticleBody(models.Model):

    id = models.AutoField(primary_key = True)
    body = models.TextField()

    readonly_fields = ('id',)

    def __str__(self):
        return "{0}".format(self.id)