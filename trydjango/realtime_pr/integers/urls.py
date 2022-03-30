from django.urls import path
from django.contrib import admin
from .views import home, index

urlpatterns = [
    path('', home, name='home'),
    path('index', index, name='index'),
]