from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from chain_store.filters import ProviderFilter
from chain_store.models import Provider
from chain_store.serializers.provider import (
    ProviderCreateSerializer,
    ProviderSerializer,
)


@extend_schema_view(
    list=extend_schema(
        description='Response list of providers',
        summary='get list of providers',
    ),
    retrieve=extend_schema(
        description='Response detail of provider',
        summary='get detail of provider',
    ),
    create=extend_schema(
        description='Create new provider',
        summary='create new provider',
    ),
    update=extend_schema(
        description='Update provider',
        summary='update provider',
    ),
    partial_update=extend_schema(
        description='Partial update provider',
        summary='partial update provider',
    ),
    destroy=extend_schema(
        description='Delete provider',
        summary='delete provider',
    ),
)
class ProviderViewSet(ModelViewSet):
    queryset = Provider.objects.all()
    serializer_default = ProviderSerializer
    serializers = {
        'create': ProviderCreateSerializer
    }

    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProviderFilter

    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializer_default)
