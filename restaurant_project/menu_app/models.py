from django.db import models
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField

class WorkingDays(models.Model):
    shift_start = models.DateTimeField()
    shift_end = models.DateTimeField()
    WORKING_DAYS_CHOICES = (
        ("Понедельник", "Понедельник"),
        ("Вторник", "Вторник"),
        ("Среда", "Среда"),
        ("Четверг", "Четверг"),
        ("Пятница", "Пятница"),
        ("Суббота", "Суббота"),
        ("Воскресенье", "Воскресенье"),

    )
    working_days = MultiSelectField(max_length=64, choices=WORKING_DAYS_CHOICES, max_choices=7)


class Reserve(models.Model):
    name = models.CharField(max_length=32)
    contact = PhoneNumberField(region='KG', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.contact}"

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=50)
    description = models.TextField()
    address = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    opening_hours = models.ForeignKey(WorkingDays, on_delete=models.CASCADE)
    restaurant_image = models.ImageField(upload_to='restaurant_images/')

    def __str__(self):
        return f"{self.restaurant_name}, {self.address}"


class Interior(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="interior")
    interior = models.ImageField(upload_to='interior_images/')


class Category(models.Model):
    category_name = models.CharField(max_length=40)

    def __str__(self):
        return self.category_name


class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=80)
    food_description = models.TextField()
    food_price = models.PositiveSmallIntegerField(default=0)
    food_image = models.ImageField(upload_to='food_image/')

    def __str__(self):
        return f"{self.food_name} - {self.food_price}"


class Supplement(models.Model):
    supplement_name = models.CharField(max_length=64)
    food = models.ManyToManyField(Food)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.supplement_name

