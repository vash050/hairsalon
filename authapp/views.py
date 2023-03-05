from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView, DetailView, CreateView
from .models import User
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from authapp.forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    extra_context = {
        'title': 'Вход пользователя'
    }
    # success_url = reverse_lazy('mainapp:index')


class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('mainapp:index')


class UserEditView(UpdateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'avatar')
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('mainapp:index')


class UserDetailView(DetailView):
    model = User
    template_name = 'authapp/user_detail.html'
