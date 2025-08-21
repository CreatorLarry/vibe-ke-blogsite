from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from .models import Comment
from articles.models import Article


def add_comment(request, article_slug):
    """Add a comment to an article"""
    article = get_object_or_404(Article, slug=article_slug, is_published=True)
    
    if request.method == 'POST':
        # Get form data
        author_name = request.POST.get('name')
        author_email = request.POST.get('email')
        content = request.POST.get('content')
        
        # Create comment
        comment = Comment(
            article=article,
            author_name=author_name,
            author_email=author_email,
            content=content,
            ip_address=request.META.get('REMOTE_ADDR')
        )
        comment.save()
        
        # Add success message
        messages.success(request, 'Your comment has been submitted and is awaiting approval.')
        
        # Redirect to article with anchor to comments
        article_url = reverse('articles:article_detail', kwargs={'slug': article.slug})
        return redirect(article_url + '#comments')
    
    # If not POST, redirect to article
    return redirect('articles:article_detail', slug=article.slug)