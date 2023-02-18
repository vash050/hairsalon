from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import User
from django.contrib import messages
from django.urls import reverse


class LoginView(TemplateView):
    template_name = 'authapp/login.html'
    extra_context = {
        'title': 'Вход пользователя'
    }


class RegisterView(TemplateView):
    template_name = 'authapp/register.html'
    extra_context = {
        'title': 'Регистрация пользователя'
    }

    def post(self, request, *args, **kwargs):
        try:
            print(request.POST.get('username'),
                        request.POST.get('email'),
                        request.POST.get('password1'),
                        request.POST.get('password2'),
                        request.POST.get('first_name'),
                        request.POST.get('last_name'),
                        request.POST.get('password1') == request.POST.get('password2'))
            if all(
                    (
                        request.POST.get('username'),
                        request.POST.get('email'),
                        request.POST.get('password1'),
                        request.POST.get('password2'),
                        request.POST.get('first_name'),
                        request.POST.get('last_name'),
                        request.POST.get('password1') == request.POST.get('password2')
                    )
            ):
                print("tut")
                new_user = User.objects.create(
                    # username=request.POST.get('username'),
                    # first_name=request.POST.get('first_name'),
                    # last_name=request.POST.get('last_name'),
                    # email=request.POST.get('email'),
                    # avatar=request.FILES.get('avatar')
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
            return HttpResponseRedirect(reverse('authapp:register'))


class LogoutView(TemplateView):
    template_name = 'authapp/logout.html'


class EditView(TemplateView):
    template_name = 'authapp/edit.html'
