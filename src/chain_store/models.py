from django.db import models


class Contact(models.Model):
    """Contact model."""

    email = models.CharField(max_length=155, verbose_name='')
    country = models.CharField(max_length=155, verbose_name='')
    city = models.CharField(max_length=155, verbose_name='')
    street = models.CharField(max_length=155, verbose_name='')
    building_number = models.PositiveIntegerField(verbose_name='')


class Product(models.Model):
    """Product model."""

    title = models.CharField(max_length=155, verbose_name='')
    model = models.PositiveSmallIntegerField(verbose_name='')
    release_date = models.DateField(verbose_name='')


class Store(models.Model):
    """Chain store model."""

    title = models.CharField(max_length=155, verbose_name='', unique=True)
    contact = models.ForeignKey(Contact, verbose_name='', on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, verbose_name='', on_delete=models.DO_NOTHING)
    provider = models.ForeignKey('self', verbose_name='', on_delete=models.SET_NULL, null=True, blank=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='')
    at_created = models.DateTimeField(verbose_name='', auto_now_add=True)
