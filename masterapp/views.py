from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from masterapp.forms import UpdateMasterDetailForm
from masterapp.models import CompletedWork, Master


class MasterWork(DetailView):
    model = CompletedWork


class MasterPage(DetailView):
    model = Master


class MasterUpdate(UpdateView):
    model = Master
    form_class = UpdateMasterDetailForm
    success_url = reverse_lazy('mainapp:index')


class CompletedWorkCreate(CreateView):
    model = CompletedWork
    fields = '__all__'
    success_url = reverse_lazy('mainapp:gallery')
