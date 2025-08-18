from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, AuthorProfile


class AuthorProfileInline(admin.StackedInline):
    """Inline admin for AuthorProfile"""
    model = AuthorProfile
    can_delete = False
    verbose_name_plural = 'Profile'


@admin.register(Author)
class AuthorAdmin(UserAdmin):
    """Admin interface for Author model"""
    inlines = (AuthorProfileInline,)
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('-date_joined',)
    
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('bio', 'profile_image')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('bio', 'profile_image')}),
    )


@admin.register(AuthorProfile)
class AuthorProfileAdmin(admin.ModelAdmin):
    """Admin interface for AuthorProfile model"""
    list_display = ('author', 'twitter_handle', 'instagram_handle')
    search_fields = ('author__username', 'author__first_name', 'author__last_name')