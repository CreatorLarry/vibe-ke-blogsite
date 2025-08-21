from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from .models import Article, ArticleView, Advertisement, Vlog
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
    
    # Get active advertisements
    advertisements = Advertisement.objects.filter(
        is_active=True,
        start_date__lte=timezone.now(),
        end_date__gte=timezone.now()
    ).order_by('-priority', '-created_date')
    
    # Get latest vlogs
    latest_vlogs = Vlog.objects.filter(
        is_published=True
    ).order_by('-published_date')[:3]
    
    # Pagination for latest articles
    paginator = Paginator(latest_articles, 6)  # Show 6 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'featured_articles': featured_articles,
        'page_obj': page_obj,
        'categories': categories,
        'advertisements': advertisements,
        'latest_vlogs': latest_vlogs,
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
    
    # Track detailed view information
    # Get the user's IP address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')
    
    # Get user agent
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    
    # Create ArticleView record
    ArticleView.objects.create(
        article=article,
        ip_address=ip_address,
        user_agent=user_agent
    )

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
        'popular_posts': popular_posts,
    }
    return render(request, "articles/article_detail.html", context)

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


def vlog_detail(request, slug):
    """Display detailed information about a vlog"""
    vlog = get_object_or_404(Vlog, slug=slug, is_published=True)
    
    # Track view count
    vlog.view_count += 1
    vlog.save(update_fields=['view_count'])
    
    # Get related vlogs
    related_vlogs = Vlog.objects.filter(
        category=vlog.category,
        is_published=True
    ).exclude(id=vlog.id)[:3]
    
    context = {
        'vlog': vlog,
        'related_vlogs': related_vlogs,
    }
    return render(request, 'articles/vlog_detail.html', context)


def vlog_list(request):
    """Display a list of vlogs"""
    # Get all published vlogs
    vlogs = Vlog.objects.filter(is_published=True).order_by('-published_date')
    
    # Get categories for filtering
    categories = Category.objects.filter(is_active=True).order_by('order')
    
    # Pagination
    paginator = Paginator(vlogs, 6)  # Show 6 vlogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'vlogs': page_obj,
        'page_obj': page_obj,
        'categories': categories,
    }
    return render(request, 'articles/vlog_list.html', context)