from django.contrib import admin
from .models import  FoodStatic,  Users
# Register your models here.
@admin.register(FoodStatic)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['food','calories','grams']
    ordering = ['calories']

@admin.register(Users)
class UserFoodAmin(admin.ModelAdmin):
    list_display = ['user','phone','birth_date','get_foods']

    
    def get_foods(self, obj):
        return "\n".join([f.food for f in obj.food.all()])

