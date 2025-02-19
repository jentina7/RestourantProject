from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"working_days", WorkingDaysViewSet, basename="working_days-list"),
router.register(r"reserve", ReserveViewSet, basename="reserve-list"),
router.register(r"restaurant", RestaurantViewSet, basename="restaurant-list"),
# router.register(r"supplement", SupplementViewSet, basename="supplement-list"),


urlpatterns = [
    path("", include(router.urls)),

    path("interior/", InteriorListAPIView.as_view(), name="interior_list"),
    path("interior/create/", InteriorCreateAPIView.as_view(), name="interior_create"),

    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category_create/', CategoryCreateAPIView.as_view(), name='category_create'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category_detail'),

    path('food/', FoodListAPIView.as_view(), name='food_list'),
    path('food_create/', FoodCreateAPIView.as_view(), name='food_create'),
    path('food/<int:pk>/', FoodRetrieveUpdateDestroyAPIView.as_view(), name='food_detail'),

    path('main_food/', CategoryListAPIView.as_view(), name='food_list'),
    path('main_food/<int:pk>/', FoodDetailSimpleAPIView.as_view(), name='food_detail'),
]