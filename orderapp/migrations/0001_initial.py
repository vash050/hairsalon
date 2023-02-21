# Generated by Django 3.2.17 on 2023-02-18 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0001_initial'),
        ('masterapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('master_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterapp.master')),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.service')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Услуга пользователя',
                'verbose_name_plural': 'Услуги пользователям',
            },
        ),
    ]