from django.contrib.auth.models import AnonymousUser
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView
from pkg_resources import _

from masterapp.models import Master, CompletedWork


def index(request):
    title = 'главная'
    context = {"title": title}

    if Master.objects.filter(user_id=request.user.pk).exists():
        context['master'] = Master.objects.get(user_id=request.user.pk)

    return render(request, 'mainapp/index.html', context=context)


class Gallery(ListView):
    model = CompletedWork

    def get(self, request, *args, **kwargs):
        """
        добавлен в context master для меню
        """
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(
                    self.object_list, "exists"
            ):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(
                    _("Empty list and “%(class_name)s.allow_empty” is False.")
                    % {
                        "class_name": self.__class__.__name__,
                    }
                )
        context = self.get_context_data()
        context['master'] = Master.objects.get(user_id=request.user.pk)
        context['master_list'] = Master.objects.all()
        return self.render_to_response(context)


# def gallery(request):
#     title = 'примеры работ'
#     context = {"title": title}
#     if Master.objects.filter(user_id=request.user.pk).exists():
#         context['master'] = Master.objects.get(user_id=request.user.pk)
#     return render(request, 'mainapp/gallery.html', context=context)


def about(request):
    title = 'о нас'
    context = {"title": title}
    if Master.objects.filter(user_id=request.user.pk).exists():
        context['master'] = Master.objects.get(user_id=request.user.pk)
    return render(request, 'mainapp/about_us.html', context=context)


def contacts(request):
    title = 'контакты'
    context = {"title": title}
    if Master.objects.filter(user_id=request.user.pk).exists():
        context['master'] = Master.objects.get(user_id=request.user.pk)
    return render(request, 'mainapp/contacts.html', context=context)
