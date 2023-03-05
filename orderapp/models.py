from django.db import models

from authapp.models import User
from mainapp.models import Service
from masterapp.models import Master


class UserService(models.Model):
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(to=Service, on_delete=models.CASCADE)
    time_service = models.TimeField()
    date_service = models.DateField()
    master_id = models.ForeignKey(to=Master, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Услуга пользователя'
        verbose_name_plural = 'Услуги пользователям'

    def __str__(self):
        return f'заказчик: {self.user_id}, мастер: {self.master_id} - {self.service_id} - {self.time_service} {self.date_service}'
