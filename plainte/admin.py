from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('category', 'description', 'location', 'created_at', 'user')  # Champs affichés dans la liste admin
    list_filter = ('category', 'created_at')  # Filtres latéraux pour la recherche
    search_fields = ('description', 'location')  # Champs pour la barre de recherche
    date_hierarchy = 'created_at'  # Navigation par dates

    # Optionnel : Configuration des champs éditables directement depuis la liste
    fields = ('user', 'category', 'description', 'location', 'photo', 'created_at')  
    readonly_fields = ('created_at',)  # Champs non modifiables

