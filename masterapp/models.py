from django.db import models
from django.utils.translation import gettext_lazy as _, ugettext_lazy

from authapp.models import User
from mainapp.models import Service


class Master(models.Model):
    class Stuff(models.TextChoices):
        CURRENT = 'CU', _('current employee')
        VACATION = 'VA', _('vacation')
        SICK = 'SI', _('sick leave')
        DISMISSED = 'DI', _('dismissed')
        STUDENT = 'ST', _('student')

    user_id = models.OneToOneField(to=User, on_delete=models.CASCADE)
    about_me = models.TextField(blank=True)
    date_start_work = models.DateField(null=True)
    is_stuff = models.CharField(max_length=2, choices=Stuff.choices, default=Stuff.STUDENT)
    master_profissions = models.ManyToManyField(to='Profession')
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'мастер'
        verbose_name_plural = 'мастера'

    def __str__(self):
        return self.user_id.first_name

    def get_is_stuff(self):
        return self.Stuff(self.is_stuff).name


class Profession(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'профессия'
        verbose_name_plural = 'профессии'

    def __str__(self):
        return self.name


class Dokument(models.Model):
    master_id = models.ForeignKey(to=Master, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    full_description = models.TextField(blank=True)
    number_dok = models.CharField(max_length=100, blank=True)
    who_issued = models.TextField(blank=True)
    date_issued = models.DateField(blank=True)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'документ'
        verbose_name_plural = 'документы'


class CompletedWork(models.Model):
    master_id = models.ForeignKey(to=Master, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='complete_works', blank=True)
    short_description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)
    service_id = models.ForeignKey(to=Service, on_delete=models.CASCADE)
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'выполненая работа'
        verbose_name_plural = 'выполненые работы'

    def __str__(self):
        return self.short_description
