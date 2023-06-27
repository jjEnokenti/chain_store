from rest_framework.viewsets import ModelViewSet

from chain_store.models import Product
from chain_store.serializers.product import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
