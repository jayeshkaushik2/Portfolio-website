from django.urls import path
from home import views
from django.contrib import admin

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('admin/', admin.site.urls),
]