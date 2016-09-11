from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ExampleModel(models.Model):
    model_pic = models.ImageField(upload_to = 'utilities/images')