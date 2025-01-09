from django.shortcuts import render, get_object_or_404
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'Recipes/list.html', context)

def recipe_detail(request, id):
    recipe = get_object_or_404(
        Recipe,
        id=id,
        status=Recipe.Status.PUBLISHED
    )
    context = {'recipe': recipe, 'id':id}
    return render(request, 'Recipes/detail.html', context)