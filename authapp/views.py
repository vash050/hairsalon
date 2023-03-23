import requests
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView, DetailView, CreateView
from .models import User
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from authapp.forms import CustomUserCreationForm, CustomUserChangeForm
from orderapp.models import UserService


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'authapp/login.html'
    extra_context = {
        'title': 'Вход пользователя'
    }


class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    extra_context = {
        'title': 'Регистрация пользователя'
    }
    success_url = reverse_lazy('mainapp:index')


class UserEditView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name_suffix = '_edit'
    extra_context = {
        'title': 'Редактирование данных пользователя'
    }

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('authapp:user-detail', args=[self.request.user.pk])


class UserDetailView(DetailView):
    model = User
    template_name = 'authapp/user_detail.html'
    extra_context = {
        'title': 'Личный кабинет пользователя'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user_services = UserService.objects.filter(user_id_id=self.request.user.pk)
            context['user_services'] = user_services
        except Exception as ex:
            context['user_services'] = ""
        return context

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('authapp:edit', args=[self.request.user.pk])

    # def get_context_data(self, **kwargs):
    #     print(self.request.user.pk)
