from django.contrib import admin

from chain_store.models import (
    Contact,
    Product,
    Store,
)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass
