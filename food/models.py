from django.db import models
from django.conf import settings
# Create your models here.

class Food(models.Model):
    food = models.CharField(max_length=255)
    grams = models.PositiveIntegerField()
    calories = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.food


class UserFood(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField()
    food = models.ManyToManyField(Food, blank=True)