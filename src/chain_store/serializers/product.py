from rest_framework import serializers

from chain_store.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Product serializer."""
    class Meta:
        model = Product
        fields = '__all__'
