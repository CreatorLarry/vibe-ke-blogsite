from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category
from articles.models import Article


def category_list(request):
    """Display a list of all categories"""
    categories = Category.objects.filter(is_active=True).order_by('order', 'name')
    
    context = {
        'categories': categories,
    }
    return render(request, 'categories/category_list.html', context)


def category_detail(request, slug):
    """Display articles in a specific category"""
    category = get_object_or_404(Category, slug=slug, is_active=True)
    
    # Get published articles in this category
    articles = Article.objects.filter(
        category=category,
        is_published=True
    ).order_by('-published_date')
    
    # Pagination
    paginator = Paginator(articles, 10)  # Show 10 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, 'categories/category_detail.html', context)