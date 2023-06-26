from django.db import models


class Contact(models.Model):
    """Contact model."""

    email = models.CharField(max_length=155, verbose_name='Электронная почта')
    country = models.CharField(max_length=155, verbose_name='Страна')
    city = models.CharField(max_length=155, verbose_name='Город')
    street = models.CharField(max_length=155, verbose_name='Улица')
    building_number = models.PositiveIntegerField(verbose_name='Номер здания')

    def __str__(self):
        return self.email

    @property
    def full_address(self):
        return f'{self.country}, {self.city}, {self.street}, {self.building_number}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    """Product model."""

    title = models.CharField(max_length=155, verbose_name='Название')
    model = models.PositiveSmallIntegerField(verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Store(models.Model):
    """Chain store model."""

    class Level(models.IntegerChoices):
        factory = 0, 'Завод'
        retail_chain = 1, 'Розничная сеть'
        Individual_entrepreneur = 2, 'Индивидуальный предприниматель'

    title = models.CharField(max_length=155, verbose_name='Название', unique=True)
    contact = models.ForeignKey(
        Contact, verbose_name='Контакты', null=True, blank=True, on_delete=models.SET_NULL
    )
    level = models.PositiveSmallIntegerField(
        verbose_name='Уровень', choices=Level.choices, default=Level.factory
    )
    products = models.ManyToManyField(
        Product, related_name='products', verbose_name='Продукт', blank=True
    )
    provider = models.ForeignKey(
        'self', verbose_name='Поставщик', on_delete=models.SET_NULL, null=True, blank=True
    )
    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Задолженность перед поставщиком',
        default=0
    )
    at_created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объект сети'
        verbose_name_plural = 'Объекты сети'
