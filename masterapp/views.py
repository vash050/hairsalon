from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView, DeleteView

from masterapp.forms import UpdateMasterDetailForm, CompletedWorkCreateForm, UpdateUserForm, CompletedWorkUpdateForm
from masterapp.models import CompletedWork, Master


class MasterWork(DetailView):
    model = CompletedWork


class MasterPage(DetailView):
    model = Master


class MasterUpdate(TemplateView):
    template_name = 'masterapp/master_form.html'
    master = None

    def get_master(self, request):
        self.master = Master.objects.get(user_id_id=request.user.id)

    def get(self, request, *args, **kwargs):
        self.get_master(request)
        master_form = UpdateMasterDetailForm(self.request.GET or None,
                                             instance=self.master)
        user_form = UpdateUserForm(self.request.GET or None, instance=request.user)
        context = self.get_context_data(**kwargs)
        context['master_form'] = master_form
        context['user_form'] = user_form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.get_master(request)
        master_form = UpdateMasterDetailForm(request.POST, request.FILES,
                                             instance=self.master)
        user_form = UpdateUserForm(request.POST, request.FILES, instance=request.user)
        if master_form.is_valid() and user_form.is_valid():
            master_form.save()
            user_form.save()
            return redirect('mainapp:index')
        else:
            return self.render_to_response(
                self.get_context_data(
                    master_form=master_form.errors,
                    user_form=user_form.errors
                )
            )


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


class WorkUpdate(UpdateView):
    model = CompletedWork
    form_class = CompletedWorkUpdateForm
    template_name = 'masterapp/completedwork_update_form.html'
    success_url = reverse_lazy('mainapp:gallery')


class WorkDelete(DeleteView):
    model = CompletedWork
    success_url = reverse_lazy('mainapp:index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(success_url)
