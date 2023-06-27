from rest_framework import serializers

from chain_store.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """Contact serializer."""
    class Meta:
        model = Contact
        fields = '__all__'
        extra_kwargs = {
            'building_number': {'required': False},
        }
