from django.db import models

from authapp.models import User
from mainapp.models import Service
from masterapp.models import Master


class UserService(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(to=Service, on_delete=models.CASCADE)
    time = models.TimeField()
    master_id = models.ForeignKey(to=Master, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Услуга пользователя'
        verbose_name_plural = 'Услуги пользователям'
