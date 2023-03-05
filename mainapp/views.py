from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from pkg_resources import _

from masterapp.models import Master, CompletedWork


def index(request):
    title = 'главная'
    context = {"title": title}
    return render(request, 'mainapp/index.html', context=context)


class Gallery(ListView):
    model = CompletedWork


def about(request):
    title = 'о нас'
    context = {"title": title}
    return render(request, 'mainapp/about_us.html', context=context)


def contacts(request):
    title = 'контакты'
    context = {"title": title}
    return render(request, 'mainapp/contacts.html', context=context)
