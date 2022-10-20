from django.db import models

# Create your models here.

class NewsImage(models.Model):
    image = models.ImageField(upload_to="", blank=True)

    def __str__(self):
        return self.image
