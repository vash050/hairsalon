from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView

from masterapp.forms import UpdateMasterDetailForm, CompletedWorkCreateForm
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
    form_class = CompletedWorkCreateForm
    success_url = reverse_lazy('mainapp:gallery')

    def post(self, request, *args, **kwargs):

        form = self.get_form()
        if form.is_valid():
            new_completed_work = form.save(commit=False)
            new_completed_work.master_id_id = Master.objects.get(user_id_id=request.user.id).id
            new_completed_work.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
