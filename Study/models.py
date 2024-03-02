from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    start_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    min_users = models.PositiveIntegerField(default=0)
    max_users = models.PositiveIntegerField(default=10)

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    video_link = models.URLField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Group(models.Model):
    title = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    members = models.ManyToManyField(User)
