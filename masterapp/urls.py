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

import masterapp.views as masterapp

app_name = 'masterapp'

urlpatterns = [
    path('master-work/<int:pk>', masterapp.MasterWork.as_view(), name='master_work'),
    path('master-page/<int:pk>', masterapp.MasterPage.as_view(), name='master_page'),
    path('master-update/<int:pk>', masterapp.MasterUpdate.as_view(), name='master_update'),
    path('master-create-work/', masterapp.CompletedWorkCreate.as_view(), name='master_create_work'),
]
