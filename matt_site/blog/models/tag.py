from django.db import models

class Tag(models.Model):

    id = models.AutoField(primary_key = True)
    tag = models.CharField(max_length = 1000)

    def __str__(self):
        return self.tag