from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('start.html/', views.start),
    path('tutorial02.html/', views.tutorial02),
]