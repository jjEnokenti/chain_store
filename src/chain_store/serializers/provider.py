from rest_framework import serializers

from chain_store.models import Provider
from chain_store.serializers.contact import ContactSerializer
from chain_store.serializers.product import ProductSerializer


class ProviderNestedSerializer(serializers.ModelSerializer):
    """Nested provider serializer."""
    email = serializers.CharField(source='contact.email', read_only=True)
    address = serializers.CharField(source='contact.full_address', read_only=True)

    class Meta:
        model = Provider
        fields = ('title', 'level', 'email', 'address',)
        extra_kwargs = {
            'level': {'read_only': True},
            'title': {'read_only': True},
        }


class ProviderSerializer(serializers.ModelSerializer):
    """Provider main serializer."""
    provider = ProviderNestedSerializer()
    contact = ContactSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Provider
        fields = '__all__'
        extra_kwargs = {
            'level': {'read_only': True},
            'debt': {'read_only': True},
        }


class ProviderCreateSerializer(serializers.ModelSerializer):
    """Provider create serializer."""
    class Meta:
        model = Provider
        fields = '__all__'
