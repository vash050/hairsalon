"""hairsalon URL Configuration

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
from django.urls import path

import mainapp.views as mainapp
import masterapp.views as masterapp


app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('gallery', mainapp.Gallery.as_view(), name='gallery'),
    path('about', mainapp.about, name='about'),
    path('contacts', mainapp.contacts, name='contacts'),
    path('gallery/<int:pk>', mainapp.GalleryMaster.as_view(), name='gallery_master'),
    path('gallery/category/<int:pk>', mainapp.GalleryCategoryService.as_view(), name='gallery_category_service'),
    path('service', mainapp.ServiceCategoryPage.as_view(), name='service'),
    path('price', mainapp.price, name='price'),
 ]
