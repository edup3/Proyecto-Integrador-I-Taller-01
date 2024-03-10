from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(default='Description not available')
    image = models.ImageField(upload_to='library/images/')
    available = models.BooleanField(default=True)
    availability = models.DateField(null=True, blank=True)
    real_available = models.BooleanField(default=True)
    real_availability = models.DateField(null=True, blank=True)
    reserved = models.BooleanField(default=False)
    reserved_date = models.DateField(null=True, blank=True)
    total_ratings = models.IntegerField(default=0)
    sum_ratings = models.IntegerField(default=0)
    rating_average = models.DecimalField(max_digits=3, decimal_places=2, default=0)

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
