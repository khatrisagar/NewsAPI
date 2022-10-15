from distutils.command.upload import upload
from enum import auto
from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    # image = models.ImageField(upload_to="")
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



#  pip install Pillow for imagefield