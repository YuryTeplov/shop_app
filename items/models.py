from django.db import models

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=255, default="default")
    price = models.IntegerField(default=5)
    description = models.TextField(default="kekeke")
    image_url = models.ImageField(default="default.jpg")
