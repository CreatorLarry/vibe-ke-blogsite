from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsletterSubscriber, NewsletterPreference


def subscribe(request):
    """Subscribe to the newsletter"""
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        
        # Check if subscriber already exists
        try:
            subscriber = NewsletterSubscriber.objects.get(email=email)
            if subscriber.is_active:
                messages.info(request, 'You are already subscribed to our newsletter.')
            else:
                # Re-activate existing subscriber
                subscriber.is_active = True
                subscriber.first_name = first_name
                subscriber.last_name = last_name
                subscriber.save()
                messages.success(request, 'You have been re-subscribed to our newsletter.')
        except NewsletterSubscriber.DoesNotExist:
            # Create new subscriber
            subscriber = NewsletterSubscriber.objects.create(
                email=email,
                first_name=first_name,
                last_name=last_name,
                is_active=True
            )
            # Create default preferences
            NewsletterPreference.objects.create(subscriber=subscriber)
            messages.success(request, 'You have been successfully subscribed to our newsletter.')
        
        # Redirect back to the same page or home
        next_url = request.POST.get('next', '/')
        return redirect(next_url)
    
    # If not POST, redirect to home
    return redirect('articles:home')