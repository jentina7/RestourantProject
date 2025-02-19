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
        fields = ["restaurant_name", "description", "restaurant_image", "address", "email", "opening_hours" ]


class RestaurantInteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ["restaurant_name", "restaurant_image" ]


class InteriorSerializer(serializers.ModelSerializer):
    restaurant = RestaurantInteriorSerializer()
    class Meta:
        model = Interior
        fields = ["interior", "restaurant"]


class InteriorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interior
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'


class SupplementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplement
        fields = '__all__'


