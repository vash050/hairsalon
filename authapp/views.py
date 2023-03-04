from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView, DetailView
from .models import User, UserProfile
from django.contrib import messages
from django.urls import reverse, reverse_lazy


class LoginView(LoginView):
    redirect_authenticated_user = True
    extra_context = {
        'title': 'Вход пользователя'
    }
    # success_url = reverse_lazy('mainapp:index')


class RegisterView(TemplateView):
    redirect_authenticated_user = True
    template_name = 'authapp/register.html'
    extra_context = {
        'title': 'Регистрация пользователя'
    }

    def post(self, request, *args, **kwargs):
        print(request.POST)
        try:
            if all(
                    (
                            request.POST.get('phone'),
                            request.POST.get('email'),
                            request.POST.get('password1'),
                            request.POST.get('password2'),
                            request.POST.get('first_name'),
                            request.POST.get('last_name'),
                            request.POST.get('password1') == request.POST.get('password2')
                    )
            ):
                new_user = User.objects.create(
                    username=request.POST.get('phone'),
                    phone=request.POST.get('phone'),
                    first_name=request.POST.get('first_name'),
                    last_name=request.POST.get('last_name'),
                    email=request.POST.get('email'),
                    avatar=request.FILES.get('avatar')
                )
                print(new_user)
                new_user.set_password(request.POST.get('password1'))
                new_user.save()
                messages.add_message(request, messages.INFO, 'Регистрация прошла успешно')
                return HttpResponseRedirect(reverse('authapp:login'))
            else:
                messages.add_message(request,
                                     messages.WARNING,
                                     'Что-то пошло не так.')
                return HttpResponseRedirect(reverse('authapp:register'))
        except Exception as ex:
            messages.add_message(request,
                                 messages.WARNING,
                                 'Что-то пошло не так.')
            return HttpResponseRedirect(reverse('mainapp:index'))


class UserEditView(UpdateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'phone', 'email', 'avatar')
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('mainapp:index')


class UserDetailView(DetailView):
    model = User
    template_name = 'authapp/user_detail.html'
