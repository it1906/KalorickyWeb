from django.urls import path
from web import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Recipe', views.RecipeListView.as_view(), name='recepty'),
    path('Recipe/<int:id>', views.RecipeDetailView.as_view(),name='recept-detail')
]