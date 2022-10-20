from distutils.command.upload import upload
from enum import auto
from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    imageUrl = models.URLField()
    description = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.title




#  pip install Pillow for imagefield