from django.contrib.auth.models import AbstractUser
from django.db import models
from food.models import Food

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    food = models.ManyToManyField(Food, blank=True)