from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin interface for Category model"""
    list_display = ('name', 'slug', 'order', 'is_active', 'article_count')
    list_filter = ('is_active', 'created_date')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('order', 'name')
    
    def article_count(self, obj):
        """Display the number of articles in this category"""
        return obj.article_count()
    article_count.short_description = 'Articles'