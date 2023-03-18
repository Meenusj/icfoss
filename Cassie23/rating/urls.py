from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('rating', views.home, name="rating"),
]