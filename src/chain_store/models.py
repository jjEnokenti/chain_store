from django.db import models


class Contact(models.Model):
    """Contact model."""

    email = models.CharField(max_length=155, verbose_name='Электронная почта')
    country = models.CharField(max_length=155, verbose_name='Страна')
    city = models.CharField(max_length=155, verbose_name='Город')
    street = models.CharField(max_length=155, verbose_name='Улица')
    building_number = models.PositiveIntegerField(verbose_name='Номер здания')


class Product(models.Model):
    """Product model."""

    title = models.CharField(max_length=155, verbose_name='Название')
    model = models.PositiveSmallIntegerField(verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода')


class Store(models.Model):
    """Chain store model."""

    title = models.CharField(max_length=155, verbose_name='Название', unique=True)
    contact = models.ForeignKey(Contact, verbose_name='Контакты', on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.DO_NOTHING)
    provider = models.ForeignKey('self', verbose_name='Поставщик', on_delete=models.SET_NULL, null=True, blank=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Задолженность перед поставщиком')
    at_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
