from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('projects/', views.all_project, name='projects'),
    path('search/', views.search_view, name='search'),
    path('about/', views.about_view, name='about'),
]