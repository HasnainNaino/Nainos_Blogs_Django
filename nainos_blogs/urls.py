from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('home/', views.home , name='home'),
    path('', views.list , name='list'),
    path('detail/<int:pk>', views.detail , name='detail'),
    path('post_like/<int:pk>', views.post_like , name='like'),
    path('post/Search_results', views.search , name='search'),


]
    