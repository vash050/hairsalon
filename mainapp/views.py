from django.shortcuts import render

from masterapp.models import Master


def index(request):
    title = 'главная'
    context = {"title": title}

    master = Master.objects.get(user_id=request.user.pk)
    context["master"] = master
    return render(request, 'mainapp/index.html', context=context)


def gallery(request):
    title = 'примеры работ'
    content = {"title": title}
    return render(request, 'mainapp/gallery.html', context=content)


def about(request):
    title = 'о нас'
    content = {"title": title}
    return render(request, 'mainapp/about_us.html', context=content)


def contacts(request):
    title = 'контакты'
    content = {"title": title}
    return render(request, 'mainapp/contacts.html', context=content)
