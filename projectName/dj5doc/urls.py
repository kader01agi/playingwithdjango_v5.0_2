from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('start/', views.start),
    path('tutorial02/', views.tutorial02),
    path('codepractice/', views.codepractice),
    path('marketplace/', views.marketplace),
    path('about/', views.about),
    path('contacts/', views.contacts),
]