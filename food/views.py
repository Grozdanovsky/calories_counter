
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import  FoodStatic, FoodUser, Users
from .serializers import FoodStaticSerializer, FoodUserSerializer, UsersSerializer

# Create your views here.

class FoodUserViewSet(ModelViewSet):
    queryset = FoodUser.objects.select_related('food').select_related('user').all()
    serializer_class = FoodUserSerializer


class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class FoodStaticViewSet(ModelViewSet):
    queryset = FoodStatic.objects.all()
    serializer_class = FoodStaticSerializer


class ShowUserFoodView(APIView):

    def get(self,request,pk):
        user_food = FoodUser.objects.filter(user = pk).all()
        serializer = FoodUserSerializer(user_food, many=True)
        return Response(serializer.data)

    def delete(self,request,pk):
        user_food = FoodUser.objects.filter(user = pk).all()
        user_food.delete()
        return Response(f"Item Deleted ", status = status.HTTP_204_NO_CONTENT)



