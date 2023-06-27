from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from chain_store.models import Contact
from chain_store.serializers.contact import ContactSerializer


@extend_schema_view(
    list=extend_schema(
        description='Response list of contacts',
        summary='get list of contacts',
    ),
    retrieve=extend_schema(
        description='Response detail of contact',
        summary='get detail of contact',
    ),
    create=extend_schema(
        description='Create new contact',
        summary='create new contact',
    ),
    update=extend_schema(
        description='Update contact',
        summary='update contact',
    ),
    partial_update=extend_schema(
        description='Partial update contact',
        summary='partial update contact',
    ),
    destroy=extend_schema(
        description='Delete contact',
        summary='delete contact',
    ),
)
class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    permission_classes = (IsAuthenticated,)
