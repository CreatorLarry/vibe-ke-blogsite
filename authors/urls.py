from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.author_list, name='author_list'),
    path('<int:pk>/', views.author_detail, name='author_detail'),
]