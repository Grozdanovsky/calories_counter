from django.contrib import admin
from .models import Food, UserFood
# Register your models here.
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['food','calories','grams']
    ordering = ['calories']

@admin.register(UserFood)
class UserFoodAmin(admin.ModelAdmin):
    list_display = ['user','phone','birth_date','get_foods']

    
    def get_foods(self, obj):
        return "\n".join([f.food for f in obj.food.all()])

