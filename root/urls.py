"""rush00 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'root'
urlpatterns = [
    path('', views.index, name='index'),

    path('worldmap/', views.worldmap, name='worldmap'),
    path('worldmap/<str:new>', views.worldmap, name='worldmap'),

    path('moviedex/', views.moviedex, name='moviedex'),
    path('moviedex/<str:action>', views.moviedex, name='moviedex'),

    path('options/', views.options, name='options'),
    path('options/save_game/<int:slot>', views.save_game, name='save_game'),
    path('options/save_game/', views.save_game, name='save_game'),

    path('options/load_game/', views.load_game, name='load_game'),
    path('options/load_game/<int:slot>', views.load_game, name='load_game'),

    path('detail/<str:moviemon_id>', views.detail, name='detail'),

    path('battle/<str:moviemon_id>', views.battle, name='battle'),

    path('super_test', views.index, name='super_test'),

]
