from django.contrib import admin
from django.utils.html import format_html
from .models import Article, ArticleView


class ArticleViewInline(admin.TabularInline):
    """Inline admin for ArticleView"""
    model = ArticleView
    extra = 0
    readonly_fields = ('ip_address', 'user_agent', 'viewed_at')
    can_delete = False


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """Admin interface for Article model"""
    list_display = ('title', 'author', 'category', 'is_featured', 'is_published', 'published_date', 'view_count')
    list_filter = ('is_featured', 'is_published', 'category', 'author', 'published_date')
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_date', 'updated_date', 'view_count')
    filter_horizontal = ()
    inlines = [ArticleViewInline]
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'excerpt', 'content')
        }),
        ('Categorization', {
            'fields': ('author', 'category')
        }),
        ('Media', {
            'fields': ('featured_image',)
        }),
        ('Publishing', {
            'fields': ('is_featured', 'is_published', 'published_date')
        }),
        ('Metadata', {
            'fields': ('created_date', 'updated_date', 'view_count'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['make_published', 'make_unpublished', 'make_featured', 'make_unfeatured']
    
    def make_published(self, request, queryset):
        """Mark selected articles as published"""
        updated = queryset.update(is_published=True)
        self.message_user(request, f'{updated} articles were successfully marked as published.')
    make_published.short_description = "Mark selected articles as published"
    
    def make_unpublished(self, request, queryset):
        """Mark selected articles as unpublished"""
        updated = queryset.update(is_published=False)
        self.message_user(request, f'{updated} articles were successfully marked as unpublished.')
    make_unpublished.short_description = "Mark selected articles as unpublished"
    
    def make_featured(self, request, queryset):
        """Mark selected articles as featured"""
        updated = queryset.update(is_featured=True)
        self.message_user(request, f'{updated} articles were successfully marked as featured.')
    make_featured.short_description = "Mark selected articles as featured"
    
    def make_unfeatured(self, request, queryset):
        """Mark selected articles as unfeatured"""
        updated = queryset.update(is_featured=False)
        self.message_user(request, f'{updated} articles were successfully marked as unfeatured.')
    make_unfeatured.short_description = "Mark selected articles as unfeatured"


@admin.register(ArticleView)
class ArticleViewAdmin(admin.ModelAdmin):
    """Admin interface for ArticleView model"""
    list_display = ('article', 'ip_address', 'viewed_at')
    list_filter = ('viewed_at', 'article__category')
    search_fields = ('article__title', 'ip_address')
    readonly_fields = ('article', 'ip_address', 'user_agent', 'viewed_at')
    
    def has_add_permission(self, request):
        """Prevent adding new article views through admin"""
        return False