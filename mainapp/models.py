from django.db import models


class Hall(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField
    full_description = models.TextField

    class Meta:
        verbose_name = 'зал'
        verbose_name_plural = 'залы'

    def __str__(self):
        return self.name


class CategoryService(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField
    full_description = models.TextField
    hall = models.ForeignKey(to=Hall, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'категория услуг'
        verbose_name_plural = ' категории услуг'

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField
    full_description = models.TextField
    category_service = models.ForeignKey(to=CategoryService, on_delete=models.CASCADE)
    price = models.DecimalField
    duration = models.IntegerField  # время на оказание услуги в минутах

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'

    def __str__(self):
        return self.name
