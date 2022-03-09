from rest_framework.viewsets import ModelViewSet
from .models import UserFood
from .serializers import FoodSerializer, UserFoodSerializer

from .models import Food
# Create your views here.

class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class UserFoodViewSet(ModelViewSet):
    queryset = UserFood.objects.all()
    serializer_class = UserFoodSerializer