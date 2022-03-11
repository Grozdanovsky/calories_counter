
from rest_framework import serializers
from .models import FoodStatic, FoodUser ,Users



class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id','phone','birth_date']


class FoodStaticSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodStatic
        fields = ['id','food','grams','calories']

class FoodUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodUser
        fields = ['id','food','user']


