from django.db import models
from django.urls import reverse
from articles.models import Article
from authors.models import Author


class Comment(models.Model):
    """Model representing a comment on an article"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField(max_length=100, help_text="Name of the comment author")
    author_email = models.EmailField(help_text="Email of the comment author")
    content = models.TextField(help_text="Comment content")
    is_approved = models.BooleanField(default=False, help_text="Is this comment approved for public display?")
    created_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True, help_text="IP address of commenter")
    
    class Meta:
        ordering = ['created_date']
        verbose_name_plural = "Comments"
    
    def __str__(self):
        return f'Comment by {self.author_name} on {self.article.title}'
    
    def get_absolute_url(self):
        """Return the URL for the article this comment is on"""
        return reverse('articles:article_detail', kwargs={'slug': self.article.slug}) + f'#comment-{self.pk}'