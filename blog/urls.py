from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', views.index),
    path('category/<str:slug>/', views.category_page),
    path('', views.PostList.as_view()),
    # path('/<int:pk>', views.single_post_page),
    path('<int:pk>/', views.PostDetail.as_view()),
]
