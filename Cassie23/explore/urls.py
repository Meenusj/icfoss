from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('explore', views.home, name="explore"),
]