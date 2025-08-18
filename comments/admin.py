from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin interface for Comment model"""
    list_display = ('author_name', 'article', 'is_approved', 'created_date')
    list_filter = ('is_approved', 'created_date', 'article__category')
    search_fields = ('author_name', 'author_email', 'content')
    readonly_fields = ('created_date', 'ip_address')
    actions = ['approve_comments', 'disapprove_comments']
    
    def approve_comments(self, request, queryset):
        """Approve selected comments"""
        updated = queryset.update(is_approved=True)
        self.message_user(request, f'{updated} comments were successfully approved.')
    approve_comments.short_description = "Approve selected comments"
    
    def disapprove_comments(self, request, queryset):
        """Disapprove selected comments"""
        updated = queryset.update(is_approved=False)
        self.message_user(request, f'{updated} comments were successfully disapproved.')
    disapprove_comments.short_description = "Disapprove selected comments"