from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import RegexValidator
from masterapp.models import Master


class User(AbstractUser):
    # first_name = models.CharField(_('Имя'), max_length=30, blank=True)
    # last_name = models.CharField(_('Фамилия'), max_length=50, blank=True)
    email = models.EmailField(_('Email'), blank=True, unique=True)
    # date_joined = models.DateTimeField(_('Дата создания'), default=timezone.now)
    # закомментированые поля определены в auth/models
    # password = models.CharField(_("password"), max_length=128)
    avatar = models.ImageField(upload_to='users', blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserProfile(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    date_born = models.DateField(blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # Validators should be a list
    email = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    additions = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


class UserService(models.Model):
    user_id = models.ForeignKey(to='User', on_delete=models.CASCADE)
    # service_id = models.ForeignKey(to='Service', on_delete=models.CASCADE)
    time = models.TimeField()
    # master_id = models.ForeignKey(to='Master', on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Услуга пользователя'
        verbose_name_plural = 'Услуги пользователям'

