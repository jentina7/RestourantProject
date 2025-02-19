from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets, generics


class WorkingDaysViewSet(viewsets.ModelViewSet):
    queryset = WorkingDays.objects.all()
    serializer_class = WorkingDaysSerializer


class ReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ReserveSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class InteriorListAPIView(generics.ListAPIView):
    queryset = Interior.objects.all()
    serializer_class = InteriorSerializer


class InteriorCreateAPIView(generics.CreateAPIView):
    queryset = Interior.objects.all()
    serializer_class = InteriorCreateSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class SupplementViewSet(viewsets.ModelViewSet):
    queryset = Supplement.objects.all()
    serializer_class = SupplementSerializer
