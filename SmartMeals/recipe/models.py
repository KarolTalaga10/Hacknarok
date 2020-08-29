from django.db import models
import json


# Create your models here.
class Ingredient(models.Model):
    name            = models.CharField(max_length=100)
    tag             = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class OwnIngredient(models.Model):
    name            = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name            = models.CharField(max_length=200)
    minutes         = models.IntegerField() 
    n_steps         = models.IntegerField() 
    steps           = models.TextField()
    ingredients     = models.TextField()
    n_ingredients   = models.IntegerField()

    def __str__ (self):
        return self.name

    def set_steps(self, x):
        self.steps = json.dumps(x)

    def get_steps(self):
        return json.loads(self.steps)

    def set_ingredients(self, x):
        self.steps = json.dumps(x)

    def get_ingredients(self):
        return json.loads(self.steps)


class Nutrition(models.Model):
    container       = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    calories        = models.DecimalField(max_digits=5, decimal_places=1)
    total_fat       = models.DecimalField(max_digits=5, decimal_places=1)
    protein         = models.DecimalField(max_digits=5, decimal_places=1)
    carbohydrates   = models.DecimalField(max_digits=5, decimal_places=1)