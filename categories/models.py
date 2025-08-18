from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    """Model representing a blog category"""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True, help_text="Description of the category")
    icon = models.CharField(max_length=50, blank=True, help_text="Icon class for UI representation (e.g., fas fa-utensils)")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """Auto-generate slug from name if not provided"""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        """Return the URL for this category"""
        return reverse('categories:category_detail', kwargs={'slug': self.slug})
    
    def article_count(self):
        """Return the number of published articles in this category"""
        return self.articles.filter(is_published=True).count()