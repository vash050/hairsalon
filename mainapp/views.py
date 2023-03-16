from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

from mainapp.models import CategoryService
from masterapp.models import Master, CompletedWork


def index(request):
    title = 'главная'
    context = {"title": title}
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


def about(request):
    title = 'о нас'
    context = {"title": title}
    return render(request, 'mainapp/about_us.html', context=context)


def contacts(request):
    title = 'контакты'
    context = {"title": title}
    return render(request, 'mainapp/contacts.html', context=context)


# def service(request):
#     title = 'услуги'
#     context = {"title": title}
#     return render(request, 'mainapp/categoryservice_list.html', context=context)


def price(request):
    title = 'price'
    context = {"title": title}
    return render(request, 'mainapp/price.html', context=context)


class ServiceCategoryPage(ListView):
    model = CategoryService
