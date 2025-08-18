from django.db import models


class NewsletterSubscriber(models.Model):
    """Model representing a newsletter subscriber"""
    email = models.EmailField(unique=True, help_text="Subscriber's email address")
    first_name = models.CharField(max_length=50, blank=True, help_text="Subscriber's first name")
    last_name = models.CharField(max_length=50, blank=True, help_text="Subscriber's last name")
    is_active = models.BooleanField(default=True, help_text="Is this subscription active?")
    subscribed_date = models.DateTimeField(auto_now_add=True)
    unsubscribed_date = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Newsletter Subscribers"
        ordering = ['-subscribed_date']
    
    def __str__(self):
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name} ({self.email})"
        return self.email
    
    def full_name(self):
        """Return the full name of the subscriber"""
        return f"{self.first_name} {self.last_name}".strip()


class NewsletterPreference(models.Model):
    """Model representing subscriber preferences for newsletter content"""
    subscriber = models.OneToOneField(NewsletterSubscriber, on_delete=models.CASCADE, related_name='preferences')
    receive_weekly = models.BooleanField(default=True, help_text="Receive weekly newsletter")
    receive_monthly = models.BooleanField(default=True, help_text="Receive monthly newsletter")
    receive_events = models.BooleanField(default=True, help_text="Receive events content")
    receive_food = models.BooleanField(default=True, help_text="Receive food content")
    receive_spots = models.BooleanField(default=True, help_text="Receive new spots content")
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Newsletter Preferences"
    
    def __str__(self):
        return f"Preferences for {self.subscriber.email}"