from django_filters import rest_framework as fil

from chain_store.models import Provider


class ProviderFilter(fil.FilterSet):
    """Filter by country fo providers"""
    country = fil.CharFilter(field_name='contact__country', lookup_expr='icontains')

    class Meta:
        model = Provider
        fields = ('country',)
