from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView, DetailView, CreateView
from .models import User
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from authapp.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'authapp/login.html'
    extra_context = {
        'title': 'Вход пользователя'
    }


class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('mainapp:index')


class UserEditView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name_suffix = '_edit'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('authapp:user-detail', args=[self.request.user.pk])


class UserDetailView(DetailView):
    model = User
    template_name = 'authapp/user_detail.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('authapp:edit', args=[self.request.user.pk])
