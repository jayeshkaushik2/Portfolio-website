from django.urls import path
from . import views

urlpatterns = [
    path('getposts/', views.getPosts, name='posts'),
    path('getposts/<str:pk>/', views.getPost, name='post'),
    path('getprofile/', views.getProfile, name='profile'),

    # path for admin login
    path('admin-panel/<str:pk>/', views.admin_login, name='admin-panel')
]