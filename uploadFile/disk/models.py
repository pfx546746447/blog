from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UploadModel(models.Model):
    username = models.CharField(max_length=100)
    img = models.FileField(upload_to='./avatar/')
