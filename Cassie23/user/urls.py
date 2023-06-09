from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('authenticate',views.authenticate, name="authenticate"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('logout',views.logout, name="logout"),
    path('map',views.map, name="map"),
    path('destinationInfo',views.destinationInfo, name="destinationInfo")
]