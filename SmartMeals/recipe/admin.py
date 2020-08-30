from django.contrib import admin

# Register your models here.
from .models import Recipe, Nutrition, OwnIngredient, Ingredient, Time

admin.site.register(Recipe)
admin.site.register(Nutrition)
admin.site.register(OwnIngredient)
admin.site.register(Ingredient)
admin.site.register(Time)