from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView

from masterapp.forms import UpdateMasterDetailForm, CompletedWorkCreateForm, UpdateUserForm
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
            return render(request, "mainapp/index.html")
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
