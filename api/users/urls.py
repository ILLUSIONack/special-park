from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('car/', views.user_car),
    path('edit_car/<str:license_plate>', views.edit_car),
    path('userinfo/', views.user_info),
]