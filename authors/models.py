from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.text import slugify


class Author(AbstractUser):
    """Custom Author model extending Django's AbstractUser"""
    bio = models.TextField(blank=True, help_text="Author's biography")
    profile_image = models.ImageField(upload_to='authors/profiles/', blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse('authors:author_detail', kwargs={'pk': self.pk})
    
    def article_count(self):
        """Return the number of published articles by this author"""
        return self.articles.filter(is_published=True).count()


class AuthorProfile(models.Model):
    """Extended profile information for authors"""
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='profile')
    website = models.URLField(blank=True, help_text="Author's personal website")
    twitter_handle = models.CharField(max_length=50, blank=True, help_text="Twitter handle without @")
    facebook_url = models.URLField(blank=True, help_text="Full Facebook profile URL")
    instagram_handle = models.CharField(max_length=50, blank=True, help_text="Instagram handle without @")
    linkedin_url = models.URLField(blank=True, help_text="Full LinkedIn profile URL")
    
    def __str__(self):
        return f"Profile for {self.author.username}"