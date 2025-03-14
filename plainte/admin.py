from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('category', 'description', 'location', 'created_at', 'user')  
    list_filter = ('category', 'created_at')  
    search_fields = ('description', 'location') 
    date_hierarchy = 'created_at' 

    fields = ('user', 'category', 'description', 'location', 'created_at')  
    readonly_fields = ('created_at',)  

