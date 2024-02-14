from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(default='Description not available')
    image = models.ImageField(upload_to='library/images/')
    available = models.BooleanField(default=True)
    availability = models.DateField(null=True, blank=True)
