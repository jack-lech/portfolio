from django.urls import path
from django.contrib import admin
from base import views

urlpatterns = [
    path('', views.home, name='main'),
]