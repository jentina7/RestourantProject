from .models import Restaurant, Category, Food, Supplement
from modeltranslation.translator import TranslationOptions,register

@register(Restaurant)
class RestaurantTranslationOptions(TranslationOptions):
    fields = ('restaurant_name', 'description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(Food)
class FoodTranslationOptions(TranslationOptions):
    fields = ('food_name', 'food_description')


@register(Supplement)
class SupplementTranslationOptions(TranslationOptions):
    fields = ('supplement_name', )

