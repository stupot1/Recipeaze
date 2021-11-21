from django.db import models
from django.db.models.base import Model

# Create your models here.

class Recipe(models.Model):
    recipe_text = models.TextField()

class Ingredient(models.Model):
    ingredient_text = models.TextField()

class Tag(models.Model):
    tag_text = models.TextField()
