from django.contrib import admin
from .models import NewsletterSubscriber, NewsletterPreference


class NewsletterPreferenceInline(admin.StackedInline):
    """Inline admin for NewsletterPreference"""
    model = NewsletterPreference
    can_delete = False
    verbose_name_plural = 'Preferences'


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    """Admin interface for NewsletterSubscriber model"""
    list_display = ('email', 'full_name', 'is_active', 'subscribed_date')
    list_filter = ('is_active', 'subscribed_date')
    search_fields = ('email', 'first_name', 'last_name')
    readonly_fields = ('subscribed_date', 'unsubscribed_date')
    inlines = [NewsletterPreferenceInline]
    actions = ['activate_subscribers', 'deactivate_subscribers']
    
    def activate_subscribers(self, request, queryset):
        """Activate selected subscribers"""
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} subscribers were successfully activated.')
    activate_subscribers.short_description = "Activate selected subscribers"
    
    def deactivate_subscribers(self, request, queryset):
        """Deactivate selected subscribers"""
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} subscribers were successfully deactivated.')
    deactivate_subscribers.short_description = "Deactivate selected subscribers"


@admin.register(NewsletterPreference)
class NewsletterPreferenceAdmin(admin.ModelAdmin):
    """Admin interface for NewsletterPreference model"""
    list_display = ('subscriber', 'receive_weekly', 'receive_monthly', 'receive_events', 'receive_food', 'receive_spots')
    list_filter = ('receive_weekly', 'receive_monthly', 'receive_events', 'receive_food', 'receive_spots')
    search_fields = ('subscriber__email', 'subscriber__first_name', 'subscriber__last_name')