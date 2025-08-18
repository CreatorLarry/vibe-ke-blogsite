from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Article
from categories.models import Category
from authors.models import Author


def home(request):
    """Display the homepage with featured articles carousel and latest articles"""
    # Get featured articles for carousel
    featured_articles = Article.objects.filter(
        is_published=True,
        is_featured=True
    ).order_by('-published_date')[:5]
    
    # Get latest articles
    latest_articles = Article.objects.filter(
        is_published=True
    ).order_by('-published_date')
    
    # Get categories for filtering
    categories = Category.objects.filter(is_active=True).order_by('order')
    
    # Pagination for latest articles
    paginator = Paginator(latest_articles, 6)  # Show 6 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'featured_articles': featured_articles,
        'page_obj': page_obj,
        'categories': categories,
    }
    return render(request, 'articles/home.html', context)


def article_detail(request, slug):
    """Display detailed information about an article"""
    article = get_object_or_404(Article, slug=slug, is_published=True)

    # Get related articles
    related_articles = article.get_related_articles()

    # Track view count (simple implementation)
    article.view_count += 1
    article.save(update_fields=['view_count'])

    # ✅ Get only approved comments
    approved_comments = article.comments.filter(is_approved=True)
    approved_comments_count = approved_comments.count()
    
    # Get related popular posts (same category, published)
    popular_posts = (
        article.category.articles.filter(is_published=True)
        .exclude(id=article.id)[:3]  # Exclude current article, limit 3
    )

    context = {
        'article': article,
        'related_articles': related_articles,
        'approved_comments': approved_comments,
        'approved_comments_count': approved_comments_count,
    }
    return render(request, "articles/article_detail.html", {
        "article": article,
        "popular_posts": popular_posts,
    })

def search(request):
    """Search articles by keyword"""
    query = request.GET.get('q')
    articles = []
    
    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) | 
            Q(excerpt__icontains=query),
            is_published=True
        ).order_by('-published_date').distinct()
    
    # Pagination
    paginator = Paginator(articles, 10)  # Show 10 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'query': query,
        'page_obj': page_obj,
    }
    return render(request, 'articles/search_results.html', context)


def about(request):
    """Display the about page"""
    return render(request, 'articles/about.html')


def contact(request):
    """Display the contact page with form"""
    if request.method == 'POST':
        # Process contact form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Here you would typically send an email or save to database
        # For now, we'll just render a success message
        context = {
            'name': name,
            'success': True,
        }
        return render(request, 'articles/contact.html', context)
    
    return render(request, 'articles/contact.html')