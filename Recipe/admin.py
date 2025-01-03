from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'created',)
    list_filter = ('created','status')
    search_fields = ('title','status')
    raw_id_fields =['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'created', 'title']
    show_facets = admin.ShowFacets.ALWAYS
