from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('list/',views.list, name='list'),
    path('add_update/',views.add_update, name='add_update'),
    path('view_recipe/',views.view_recipe, name='view_recipe'),
]