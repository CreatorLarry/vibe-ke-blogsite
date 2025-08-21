from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('vlog/<slug:slug>/', views.vlog_detail, name='vlog_detail'),
    path('vlogs/', views.vlog_list, name='vlog_list'),
]