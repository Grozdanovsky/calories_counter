from django.db import models
from django.conf import settings
# Create your models here.

class Users(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self) -> str:
        return f'{self.user.first_name} , {self.user.last_name}'
    

class FoodStatic(models.Model):
    food = models.CharField(max_length=255)
    grams = models.PositiveIntegerField()
    calories = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.food


class FoodUser(models.Model):
    food = models.ForeignKey(FoodStatic, on_delete=models.PROTECT)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.food
