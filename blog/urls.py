from django.urls import path

from . import views # Imports views.py from current directory

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
]