from django.urls import path
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router = routers.SimpleRouter()
router.register(r'get-posts', views.Getpost, basename='posts')

urlpatterns = [
    # path('get-posts/', views.getPosts, name='posts'),
    path('get-posts/<str:pk>/', views.getPost, name='post'),

    # path for profile login
    path('get-profile/', views.getProfile, name='profile'),

    # path for admin login
    path('get-admin/<str:pk>/', views.admin_login, name='admin'),

    # path for social links
    path('get-sociallinks/', views.getSocialLink, name='sociallinks'),

    # path for education details
    path('get-education/', views.getEducation, name='educations'),

    #path for experience details
    path('get-experience/', views.getExperience, name='experiences'),

    #path for skill details
    path('get-skill/', views.getSkill, name='skills'),

    #path for project details
    path('get-project/', views.getProject, name='projects'),

    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += router.urls