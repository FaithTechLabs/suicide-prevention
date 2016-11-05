from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Reason(models.Model):
    title = models.CharField(max_length=200, default='')
    keywords = models.TextField()
    resources = models.TextField()
    response = models.TextField()

    def __str__(self):
        return u"%s" % (self.title)
