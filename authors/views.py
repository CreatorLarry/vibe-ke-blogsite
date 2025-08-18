from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Author


def author_list(request):
    """Display a list of all authors"""
    authors = Author.objects.filter(is_active=True).order_by('last_name')
    
    # Pagination
    paginator = Paginator(authors, 10)  # Show 10 authors per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'authors/author_list.html', context)


def author_detail(request, pk):
    """Display detailed information about an author"""
    author = get_object_or_404(Author, pk=pk, is_active=True)
    
    # Get published articles by this author
    articles = author.articles.filter(is_published=True).order_by('-published_date')
    
    # Pagination for articles
    paginator = Paginator(articles, 5)  # Show 5 articles per page
    page_number = request.GET.get('page')
    articles_page = paginator.get_page(page_number)
    
    context = {
        'author': author,
        'articles_page': articles_page,
    }
    return render(request, 'authors/author_detail.html', context)