from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from chain_store.models import (
    Contact,
    Product,
    Provider,
)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Add contact to admin panel."""
    list_display = ('email', 'full_address',)
    list_filter = ('email', 'city', 'country', 'street',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Add product to admin panel."""
    list_display = ('title', 'model', 'release_date',)
    list_filter = ('title', 'model', 'release_date',)


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    """
    Add provider to admin panel.

    methods:
        provider_ling - return child provider link
        clear_debt - clears the debt owed to the provider
    """
    list_display = (
        'title',
        'contact',
        'provider_link',
        'debt',
        'at_created',
    )
    list_filter = ('contact__city',)
    actions = ('clear_debt',)

    @admin.display(description='Поставщик')
    def provider_link(self, obj):
        provider = obj.provider

        if provider:
            url = reverse('admin:chain_store_provider_change', args=[provider.id])

            return format_html(f'<a href={url}>{provider.title}</a>')

        return 'Нет поставщика'

    @admin.action(description='Очистить задолженность перед поставщиком')
    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
