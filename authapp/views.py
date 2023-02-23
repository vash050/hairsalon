from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, UpdateView
from .models import User
from django.contrib import messages
from django.urls import reverse, reverse_lazy


# class CustomLoginView(LoginView):
#     redirect_authenticated_user = True
#     template_name = 'authapp/login.html'
#     extra_context = {
#         'title': 'Вход пользователя'
#     }
#
#     success_url = reverse_lazy('mainapp:index')


class RegisterView(TemplateView):
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


class CustomLogoutView(LogoutView):
    template_name = 'authapp/logout.html'


    # class EditView(TemplateView):
    #     template_name = 'authapp/user_profile.html'
    #     extra_context = {'title': 'Профиль пользователя', "user": User.objects.get(phone="8-999-999999")}
    #
    #     def post(self, request, *args, **kwargs):
    #         # if request.POST.get('username'):
    #         #     request.user.username = request.POST.get('username')
    #         #
    #         # if request.POST.get('first_name'):
    #         #     request.user.username = request.POST.get('first_name')
    #         #
    #         # if request.POST.get('last_name'):
    #         #     request.user.username = request.POST.get('last_name')
    #         #
    #         # if request.POST.get('phone'):
    #         #     request.user.username = request.POST.get('phone')
    #         #
    #         # request.user.save()
    #         return self.extra_context
    #         # return HttpResponseRedirect(reverse('authapp:edit'))


class EditView(UpdateView):
    model = User
    fields = ('username', 'phone', 'email', 'avatar')
    success_url = reverse_lazy('mainapp:index')

