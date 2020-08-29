from django.contrib import admin

# Register your models here.
from .models import Recipe, Nutrition

admin.site.register(Recipe)
admin.site.register(Nutrition)