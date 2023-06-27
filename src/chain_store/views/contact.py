from rest_framework.viewsets import ModelViewSet

from chain_store.models import Contact
from chain_store.serializers.contact import ContactSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
