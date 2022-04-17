from django.urls import path
from . import views

urlpatterns = [
    path('get-posts/', views.getPosts, name='posts'),
    path('get-posts/<str:pk>/', views.getPost, name='post'),
    path('get-profile/', views.getProfile, name='profile'),

    # path for admin login
    path('get-admin/<str:pk>/', views.admin_login, name='admin'),

    # path for social links
    path('get-sociallinks/', views.getSocialLink, name='sociallinks'),
]