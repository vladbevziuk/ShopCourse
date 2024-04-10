from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

class Course(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    students_amount = models.IntegerField()
    reviews_amount = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

