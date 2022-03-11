
from django import views
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('food',views.FoodStaticViewSet)
router.register('users',views.UsersViewSet)
router.register('add-food-to-user',views.FoodUserViewSet)

urlpatterns = [

    path('user-food/<int:pk>/',views.ShowUserFoodView.as_view())

]




urlpatterns += router.urls
