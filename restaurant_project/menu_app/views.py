from django.shortcuts import render
from rest_framework.filters import SearchFilter

from .models import *
from .serializers import *
from rest_framework import viewsets, generics
from .pagination import CustomPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


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


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['food_name']


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class FoodSimpleViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSimpleSerializer


# class SupplementViewSet(viewsets.ModelViewSet):
#     queryset = Supplement.objects.all()
#     serializer_class = SupplementSerializer


class FoodListAPIView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodListSerializer


class FoodCreateAPIView(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodCreateSerializer

    serializer_class = FoodSerializer
    pagination_class = CustomPagination

class FoodRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodDetailSerializer


class FoodDetailSimpleAPIView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodDetailSimpleSerializer
