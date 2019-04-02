from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('elements/', views.elements, name='elements'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('blog-home', views.blogHome, name='blog-home'),
    path('blog-details', views.blogDetails, name='blog-details'),
    path('about/', views.about, name='about'),


]
