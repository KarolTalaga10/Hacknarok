from django.http import HttpResponse
from django.shortcuts import render

from recipe.models import OwnIngredient, Recipe, Nutrition
from recipe.forms import TimeForm

# Create your views here.

def home_view(response, *args, **kwargs):
    # return HttpResponse("<h1>TEST</h1>")
    ingredients = OwnIngredient.objects.all() 
    recipes = Recipe.objects.all()
    total_ingredients = ingredients.count()
    total_recipes = recipes.count()

    form = TimeForm(response.POST or None)
    if form.is_valid():
        form.save()

    context ={
        'form':form,
        'ingredients':ingredients,
        'total_ingredients':total_ingredients,
        'total_recipes':total_recipes
    }
    return render(response, 'home.html', context)

def about_view(response, *args, **kwargs):
    return render(response, 'about.html', {})