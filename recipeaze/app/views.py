from django.shortcuts import render
from django.http import HttpResponse

# This is the Enter Page
def index(request):    
    return HttpResponse("Hello this is in app")

# This is the List Page
def list(request):
    return HttpResponse("Hello this is a list of recipes")

# This is the Add / Update Page
def add_update(request):
    return HttpResponse("Hello this is a page to Add or Update a recipe")

# This is the Recipe Page
def view_recipe(request):
    return HttpResponse("Hello this is a view of a recipe")
