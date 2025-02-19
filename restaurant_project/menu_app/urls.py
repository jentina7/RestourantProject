from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"working_days", WorkingDaysViewSet, basename="working_days-list"),
router.register(r"reserve", ReserveViewSet, basename="reserve-list"),
router.register(r"restaurant", RestaurantViewSet, basename="restaurant-list"),
router.register(r"category", CategoryViewSet, basename="category-list"),
router.register(r"food", FoodViewSet, basename="food-list"),
router.register(r"supplement", SupplementViewSet, basename="supplement-list")


urlpatterns = [
    path("", include(router.urls)),

    path("interior/", InteriorListAPIView.as_view(), name="interior_list"),
    path("interior/create/", InteriorCreateAPIView.as_view(), name="interior_create"),
]