from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Reason(models.Model):
    keywords = models.TextField()
    resources = models.TextField()
    response = models.TextField()
