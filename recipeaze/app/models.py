from django.db import models
from django.db.models.base import Model

# Create your models here.

class Ingredient(models.Model):
    ingredient_text = models.TextField()
class Recipe(models.Model):
    ingredients = models.ManyToManyField(Ingredient)
    recipe_text = models.TextField()
    tag_text = models.TextField()