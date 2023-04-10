import requests
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordContextMixin, FormView
from django.shortcuts import render, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
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
            if user_services:
                context['user_services'] = user_services
            else:
                context['user_services'] = "Null"
        except Exception as ex:
            context['user_services'] = "Ошибка данных"
        return context

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('authapp:edit', args=[self.request.user.pk])


class PasswordChangeView(PasswordContextMixin, FormView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('authapp:password_change_done')
    template_name = 'authapp/password_change_form.html'
    title = 'Смена пароля'

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        # Updating the password logs out all other sessions for the user
        # except the current one.
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)


class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
    template_name = 'authapp/password_change_done.html'
    title = 'Пароль успешно изменен'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
