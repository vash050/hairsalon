from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from mainapp.models import CategoryService, Service
from masterapp.models import Master, CompletedWork
from authapp.models import UserProfile, User
from orderapp.models import UserService
import datetime


def index(request):
    title = 'главная'
    context = {"title": title}
    service = CategoryService.objects.all()[:6]
    services = Service.objects.all()
    context['messangers'] = UserProfile.CHOICES
    context['services'] = services
    context['service'] = service
    if request.method == "POST":
        add_service_to_user(request)
    return render(request, 'mainapp/index.html', context=context)


class GalleryMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['master_list'] = Master.objects.all()
        return context


class Gallery(GalleryMixin, ListView):
    model = CompletedWork

    def get_queryset(self):
        return CompletedWork.objects.all().filter(is_active=True)


class GalleryMaster(GalleryMixin, ListView):
    model = CompletedWork

    def get_queryset(self):
        return CompletedWork.objects.filter(master_id=self.kwargs['pk']).filter(is_active=True)


class GalleryCategoryService(GalleryMixin, ListView):
    model = CompletedWork

    def get_queryset(self):
        return CompletedWork.objects.filter(service_id__category_service_id=self.kwargs['pk']).filter(is_active=True)


def about(request):
    title = 'о нас'
    context = {"title": title}
    masters = Master.objects.all()
    context['master_list'] = masters
    return render(request, 'mainapp/about_us.html', context=context)


def contacts(request):
    title = 'контакты'
    context = {"title": title}
    return render(request, 'mainapp/contacts.html', context=context)


def price(request):
    title = 'price'
    service_barbershop = Service.objects.filter(category_service__name__in=['Уход за волосами', 'Прически',
                                                                            'Окрашивание', 'Стрижка'])
    service_manicure = Service.objects.filter(category_service__name='Маникюр')
    service_pedicure = Service.objects.filter(category_service__name='Педикюр')
    context = {"title": title, 'service_barbershop': service_barbershop, 'service_manicure': service_manicure,
               'service_pedicure': service_pedicure}
    return render(request, 'mainapp/price.html', context=context)


class ServiceCategoryPage(ListView):
    model = CategoryService


def add_service_to_user(requests):
    title = 'главная'
    context = {"title": title}
    name = requests.POST.get('name')
    phone = requests.POST.get('phone')
    service = requests.POST.get('service')
    date_time = requests.POST.get('datetime')
    date_time_obj = datetime.datetime.strptime(date_time, '%Y-%m-%dT%H:%M')
    user = None
    try:
        user = User.objects.get(phone=phone)
    except User.DoesNotExist:
        print("Нет такого номера в базе")
        username = phone
        if name:
            username = name.strip() + phone
        user = User(username=username,
                    phone=phone,
                    email='%s@%s.ru' % (phone, phone)
                    )
        user.save()
    get_service = Service.objects.get(id=service)
    user_service = UserService(user_id=user,
                               service_id=get_service,
                               time_service=date_time_obj.time(),
                               date_service=date_time_obj.date(),
                               master_id=Master.objects.get(id=1)
                               )
    user_service.save()
    return render(requests, 'mainapp/index.html', context=context)
