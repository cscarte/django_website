from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('about/', views.about, name="about"),

    path('create-room/', views.createRoom, name="create-room"),
]
