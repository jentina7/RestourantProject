from rest_framework import serializers
from .models import *


class WorkingDaysSerializer(serializers.ModelSerializer):
    shift_start = serializers.DateTimeField(format="%H:%M")
    shift_end = serializers.DateTimeField(format="%H:%M")
    class Meta:
        model = WorkingDays
        fields = ["shift_start", "shift_end", "working_days"]


class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    opening_hours = WorkingDaysSerializer(read_only=True)

    class Meta:
        model = Restaurant
        fields = ["restaurant_name", "description", "restaurant_image", "address", "email", "opening_hours"]


class RestaurantInteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["restaurant_name", "restaurant_image"]


class InteriorSerializer(serializers.ModelSerializer):
    restaurant = RestaurantInteriorSerializer()

    class Meta:
        model = Interior
        fields = ["interior", "restaurant"]


class InteriorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interior
        fields = '__all__'


class SupplementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplement
        fields = ['supplement_name', 'food', 'price']


class FoodDetailSerializer(serializers.ModelSerializer):
    supplement_food = SupplementSerializer(read_only=True, many=True)

    class Meta:
        model = Food
        fields = ['food_name', 'food_description', 'food_price', 'food_image', 'supplement_food']


class FoodListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = ['food_name', 'food_description', 'food_price', 'food_image']


class FoodCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = '__all__'


class FoodSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['food_name', 'food_description', 'food_price', 'food_image']


class FoodDetailSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['food_name', 'food_description', 'food_price']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    category_food = FoodSimpleSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'category_food']





