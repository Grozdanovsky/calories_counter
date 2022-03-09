from pprint import pprint
from rest_framework import serializers
from .models import Food, UserFood

class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ['id','food','grams','calories']


class UserFoodSerializer(serializers.ModelSerializer):

    food = FoodSerializer(many = True)
    total_calories = serializers.SerializerMethodField()

    def get_total_calories(self,user):
        
        return sum(food.calories for food in user.food.all())


    
    class Meta:
        model = UserFood
        fields = ['id','user_id','phone','birth_date','food','total_calories']