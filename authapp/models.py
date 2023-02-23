from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import RegexValidator
# from masterapp.models import Master


class User(AbstractUser):
    # first_name = models.CharField(_('Имя'), max_length=30, blank=True)
    # last_name = models.CharField(_('Фамилия'), max_length=50, blank=True)
    phone_regex = RegexValidator(regex=r"[8]{1}-[0-9]{3}-[0-9]{4}",
                                 message="Phone number must be entered in the format: '8-999-99999'. Up to 10 digits allowed.")
    phone = models.CharField(_('Телефон'), unique=True, validators=[phone_regex], max_length=17, blank=True)  # Validators should be a list
    email = models.EmailField(_('Email'), blank=True, unique=True)
    avatar = models.ImageField(upload_to='users', blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserProfile(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    date_born = models.DateField(blank=True)
    telegram = models.CharField(max_length=50)
    additions = models.TextField(blank=True)
    CHOICES = (
        ('TL', 'Телефон'),
        ('WP', 'WhatsApp'),
        ('TG', 'Telegram'),
        ('SM', 'Смс'),
        ('EM', 'Email'),
    )
    favourite = models.CharField(max_length=10, choices=CHOICES)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'



