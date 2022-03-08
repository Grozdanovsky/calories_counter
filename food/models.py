from django.db import models

# Create your models here.

class Food(models.Model):
    food = models.CharField(max_length=255)
    grams = models.PositiveIntegerField()
    calories = models.PositiveIntegerField()