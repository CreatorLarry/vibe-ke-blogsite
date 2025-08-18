from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from authors.models import Author
from categories.models import Category


class Article(models.Model):
    """Model representing a blog article"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    excerpt = models.TextField(blank=True, help_text="Short summary of the article")
    content = models.TextField(help_text="Main content of the article")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='articles')
    featured_image = models.ImageField(upload_to='articles/images/', blank=True, null=True)
    is_featured = models.BooleanField(default=False, help_text="Is this a featured article?")
    is_published = models.BooleanField(default=False, help_text="Is this article published?")
    published_date = models.DateTimeField(blank=True, null=True, help_text="Date when published")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0, help_text="Number of views")
    
    class Meta:
        ordering = ['-created_date']
        verbose_name_plural = "Articles"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """Auto-generate slug from title if not provided"""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        """Return the URL for this article"""
        return reverse('articles:article_detail', kwargs={'slug': self.slug})
    
    def get_related_articles(self, count=3):
        """Get related articles based on category and tags"""
        return Article.objects.filter(
            category=self.category,
            is_published=True
        ).exclude(id=self.id)[:count]
        
    @property
    def approved_comments(self):
        return self.comments.filter(is_approved=True)


class ArticleView(models.Model):
    """Model to track article views"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='views')
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True)
    viewed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-viewed_at']
        verbose_name_plural = "Article Views"
    
    def __str__(self):
        return f"{self.article.title} viewed from {self.ip_address}"