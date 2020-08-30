from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import OwnIngredientForm
from .models import OwnIngredient, Recipe, Nutrition, Time

# Create your views here.

def add_ingredients_view(response, *args, **kwargs):
    ingredients = OwnIngredient.objects.all() 
    recipes = Recipe.objects.all()
    total_ingredients = ingredients.count()
    total_recipes = recipes.count()

    form = OwnIngredientForm(response.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    context = {
        'form':form,
        'ingredients':ingredients,
        'total_ingredients':total_ingredients,
        'total_recipes':total_recipes
    }
    return render(response, 'add_ingredients.html', context)

def delete_ingredients_view(response, pk, *args, **kwargs):
    ingredient = OwnIngredient.objects.get(id=pk) 
    ingredients = OwnIngredient.objects.all() 
    recipes = Recipe.objects.all()
    total_ingredients = ingredients.count()
    total_recipes = recipes.count()

    if response.method == "POST":
	    ingredient.delete()
	    return redirect('/')

    context = {
        'item':ingredient,
        'ingredients':ingredients,
        'total_ingredients':total_ingredients,
        'total_recipes':total_recipes
    }
    return render(response, 'delete_ingredients.html', context)