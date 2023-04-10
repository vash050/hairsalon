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
import authapp.views
from authapp.apps import AuthappConfig
from django.urls import path, include
from authapp.views import CustomLoginView, RegisterView, LogoutView, UserEditView, UserDetailView, PasswordChangeView, \
    PasswordChangeDoneView

app_name = AuthappConfig.name

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit/<int:pk>/', UserEditView.as_view(), name='edit'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('edit/password/', PasswordChangeView.as_view(), name='password_change'),
    path('edit/password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
]
