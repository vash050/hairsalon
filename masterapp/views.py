from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView

from masterapp.models import CompletedWork, Master


class MasterWork(DetailView):
    model = CompletedWork


class MasterPage(DetailView):
    model = Master


class MasterUpdate(UpdateView):
    model = Master
    fields = ['user_id', 'about_me', 'is_stuff', 'master_profissions']
