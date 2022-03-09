
from django import views
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('food',views.FoodViewSet)
router.register('food-users',views.UserFoodViewSet)



urlpatterns = router.urls
