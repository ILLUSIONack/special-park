from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.garage),
    path('port/', views.time_table),
]