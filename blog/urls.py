from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='blog'),
    path('search/', views.search_function, name='search_url'),
    path('news/<slug:slug>/', views.post_detail, name= 'post_detail_url'),
    path('news/<slug:slug>/comment/', views.comment, name= 'comment'),
    path('categories/<slug:slug>/', views.category_detail, name= 'category_detail_url'),
    path('register/', views.register, name='register'),
    path('sort/', views.sort, name='sort'),
]