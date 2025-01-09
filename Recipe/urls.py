from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipes_list' ),
    path('<int:id>/', views.recipe_detail, name='recipe_detail' ),
]