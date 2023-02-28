from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import RegexValidator


class User(AbstractUser):
    phone_regex = RegexValidator(regex=r"[8]{1}-[0-9]{3}-[0-9]{3}-[0-9]{4}",
                                 message="Формат номера телефона должен быть: '8-999-999-9999'. До 10 цифр.")
    phone = models.CharField(_('Телефон'), unique=True, validators=[phone_regex], max_length=17, blank=True)
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

    def __str__(self):
        return '%s %s' % (self.id.__getattribute__('first_name'), self.id.__getattribute__('last_name'))

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'



