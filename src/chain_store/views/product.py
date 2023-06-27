from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from chain_store.models import Product
from chain_store.serializers.product import ProductSerializer


@extend_schema_view(
    list=extend_schema(
        description='Response list of products',
        summary='get list of products',
    ),
    retrieve=extend_schema(
        description='Response detail of product',
        summary='get detail of product',
    ),
    create=extend_schema(
        description='Create new product',
        summary='create new product',
    ),
    update=extend_schema(
        description='Update product',
        summary='update product',
    ),
    partial_update=extend_schema(
        description='Partial update product',
        summary='partial update product',
    ),
    destroy=extend_schema(
        description='Delete product',
        summary='delete product',
    ),
)
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = (IsAuthenticated,)
