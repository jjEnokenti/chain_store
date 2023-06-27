from django.urls import (
    include,
    path,
)
from rest_framework.routers import SimpleRouter

from chain_store.views import provider


router_provider = SimpleRouter()
router_product = SimpleRouter()
router_contact = SimpleRouter()

router_provider.register('providers', provider.ProviderViewSet, basename='providers')
router_product.register('products', provider.ProviderViewSet, basename='products')
router_contact.register('contacts', provider.ProviderViewSet, basename='contacts')

urlpatterns = [
    path('', include(router_provider.urls)),
    path('', include(router_product.urls)),
    path('', include(router_contact.urls)),
]
