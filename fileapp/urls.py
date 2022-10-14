"""fileapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from unicodedata import name
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name= 'main'),
    path('create/', create, name = 'create'),
    path('delete/<int:id>', delete_letter, name = 'delete'),
    path('edit/<int:id>', edit_letter, name = 'edit'),
    path('cart/',  cart, name='cart'),
    path('favourites_page/', favourites_page , name = 'favourites_page'),
    path('favourites/<int:id>', favourites , name = 'favourites'),
]
