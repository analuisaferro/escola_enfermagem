from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index),
    path('editais/', views.editais, name='editais'),  
    path('edital/<id>', views.edital, name='edital'),  
    path('resultado/', views.resultado, name='resultado'),  
    path('login/', views.login_view, name='login'),  
    
]