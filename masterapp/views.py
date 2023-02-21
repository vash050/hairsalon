from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from masterapp.models import CompletedWork, Master


class MasterWork(DetailView):
    model = CompletedWork


class MasterPage(DetailView):
    model = Master


class MasterUpdate(UpdateView):
    model = Master
    fields = ['user_id', 'about_me', 'is_stuff', 'master_profissions']


class CompletedWorkCreate(CreateView):
    model = CompletedWork
    fields = '__all__'
    success_url = reverse_lazy('mainapp:gallery')
