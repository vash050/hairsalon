from django.shortcuts import render
from django.views.generic import ListView, DetailView

from masterapp.models import CompletedWork, Master


class MasterWork(DetailView):
    model = CompletedWork


class MasterPage(DetailView):
    model = Master