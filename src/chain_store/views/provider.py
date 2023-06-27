# from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from chain_store.models import Provider
from chain_store.serializers.provider import (
    ProviderCreateSerializer,
    ProviderSerializer,
)


class ProviderViewSet(ModelViewSet):
    queryset = Provider.objects.all()
    serializer_default = ProviderSerializer
    serializers = {
        'create': ProviderCreateSerializer
    }

    # filter_backends = ()
    # search_fields = ('contact__country',)

    # permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializer_default)
