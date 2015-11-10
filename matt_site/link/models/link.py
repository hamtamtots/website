from django.db import models

class Link(models.Model):

    key = models.CharField(max_length = 1000, primary_key = True)
    url = models.CharField(max_length = 1000)

    def __str__(self):
        return '{0}: {1}'.format(self.key, self.url)