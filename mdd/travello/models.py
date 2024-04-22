from django.db import models

# Create your models here.
class Destination(models.Model):
  
    name = models.CharField(max_length=150)
    description = models.TextField()
    img =models.ImageField(upload_to='pics')
    days = models.CharField(max_length=25)
    rating = models.TextField()
    offer = models.BooleanField(default=False)
