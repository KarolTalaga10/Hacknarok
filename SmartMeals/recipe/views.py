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

def search_view(response, *args, **kwargs):
    time = Time.objects.all()
    ingredients = OwnIngredient.objects.all()
    print(ingredients)
    # print(time[0].mins)
    if time:
        recipes = Recipe.objects.filter(ingredients__contains=ingredients[0], minutes__contains=time[0].mins).filter(ingredients__contains=ingredients[1]).filter(ingredients__contains=ingredients[2])
    else:
        t = Time.objects.create()
        time = Time.objects.all()
        recipes = Recipe.objects.filter(ingredients__contains=ingredients[0], minutes__contains=time[0].mins).filter(ingredients__contains=ingredients[1]).filter(ingredients__contains=ingredients[2])

    recipes = recipes[:10]
    print(recipes)
    

    ingredients.delete()
    time.delete()

    context = {
        'recipes':recipes
    }
    return render(response, 'search.html', context)

def recipe_details_view(response, pk, *args, **kwargs):
    recipe = Recipe.objects.get(id=pk)
    recipe.steps = recipe.steps.replace('[\'','')
    recipe.steps = recipe.steps.replace('\']','')
    # recipe.steps = recipe.steps.replace('###', '\r\n')
    lst_of_steps = recipe.steps.split('###')
    # print(lst_of_strings)
    recipe.ingredients = recipe.ingredients.replace('[\'','')
    recipe.ingredients = recipe.ingredients.replace('\']','')
    print(recipe.ingredients)
    lst_of_ingredients = recipe.ingredients.split('###')

    context = {
        'recipe':recipe,
        'lst_of_steps':lst_of_steps,
        'lst_of_ingredients':lst_of_ingredients
    }
    return render(response, 'recipe_details.html', context)