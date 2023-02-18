from django.shortcuts import render
from django.views.generic import ListView, DetailView

from masterapp.models import CompletedWork


class MasterWork(DetailView):
    model = CompletedWork
