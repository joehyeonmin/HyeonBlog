from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('/<int:pk>', views.single_post_page),
    path('', views.index),
]
