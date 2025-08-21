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


class Advertisement(models.Model):
    """Model representing an advertisement"""
    title = models.CharField(max_length=200, help_text="Advertisement title for admin reference")
    image = models.ImageField(upload_to='advertisements/', blank=True, null=True, help_text="Advertisement image")
    link = models.URLField(blank=True, help_text="URL to redirect to when clicked")
    content = models.TextField(blank=True, help_text="Text content for text-based ads")
    is_active = models.BooleanField(default=True, help_text="Is this advertisement active?")
    start_date = models.DateTimeField(help_text="When to start showing this advertisement")
    end_date = models.DateTimeField(help_text="When to stop showing this advertisement")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=0, help_text="Higher priority ads are shown first")
    
    class Meta:
        ordering = ['-priority', '-created_date']
        verbose_name_plural = "Advertisements"
    
    def __str__(self):
        return self.title
    
    def is_live(self):
        """Check if the advertisement is currently active and within date range"""
        from django.utils import timezone
        now = timezone.now()
        return self.is_active and self.start_date <= now <= self.end_date


class Vlog(models.Model):
    """Model representing a video blog (vlog)"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField(help_text="Description of the vlog")
    video_url = models.URLField(help_text="URL to the video (YouTube, Vimeo, etc.)")
    thumbnail = models.ImageField(upload_to='vlogs/thumbnails/', blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='vlogs')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='vlogs')
    is_featured = models.BooleanField(default=False, help_text="Is this a featured vlog?")
    is_published = models.BooleanField(default=False, help_text="Is this vlog published?")
    published_date = models.DateTimeField(blank=True, null=True, help_text="Date when published")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    view_count = models.PositiveIntegerField(default=0, help_text="Number of views")
    
    class Meta:
        ordering = ['-created_date']
        verbose_name_plural = "Vlogs"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """Auto-generate slug from title if not provided"""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        """Return the URL for this vlog"""
        return reverse('articles:vlog_detail', kwargs={'slug': self.slug})
    
    def get_video_id(self):
        """Extract video ID from YouTube URL"""
        if 'youtube.com' in self.video_url:
            import re
            match = re.search(r'v=([^&]+)', self.video_url)
            if match:
                return match.group(1)
        elif 'youtu.be' in self.video_url:
            import re
            match = re.search(r'youtu\.be/([^?]+)', self.video_url)
            if match:
                return match.group(1)
        return None
    
    def get_embed_url(self):
        """Get embed URL for the video"""
        video_id = self.get_video_id()
        if video_id:
            return f'https://www.youtube.com/embed/{video_id}'
        return self.video_url