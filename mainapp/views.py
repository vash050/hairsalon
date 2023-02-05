from django.shortcuts import render


def index(request):
    title = 'главная'
    content = {"title": title}
    return render(request, 'mainapp/index.html', context=content)


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
