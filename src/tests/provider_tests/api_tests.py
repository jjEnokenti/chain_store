import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from chain_store.serializers.provider import ProviderSerializer


@pytest.mark.django_db
class TestProviderAPI:

    def test_create_provider_with_anon(self, client, provider_level_0):
        provider = provider_level_0
        url = reverse('provider-list')

        payload = {
            'title': f'{provider.title} 123',
            'contact': provider.contact.pk,
            'products': [obj.pk for obj in provider.products.all()],
        }

        response = client.post(path=url, data=payload, content_type='application/json')

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_get_list_provider_with_anon(self, client, list_providers):
        url = reverse('provider-list')

        response = client.get(path=url)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_get_single_provider_with_anon(self, client, provider_level_1):
        provider = provider_level_1
        url = reverse('provider-detail', kwargs={'pk': provider.pk})

        response = client.get(path=url)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_update_provider_with_anon(self, client, provider_level_0):
        provider = provider_level_0
        url = reverse('provider-detail', kwargs={'pk': provider.pk})

        title = 'updated title'
        payload = {
            'title': title,
        }

        response = client.put(path=url, data=payload, content_type='application/json')

        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert provider.title != title

    def test_delete_provider_with_anon(self, client, provider_level_0):
        provider = provider_level_0
        url = reverse('provider-detail', kwargs={'pk': provider.pk})

        response = client.delete(path=url, content_type='application/json')

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_provider_ok(self, auth_client, provider_level_0):
        provider = provider_level_0
        url = reverse('provider-list')

        title = f'{provider.title} 123'
        products = [obj.pk for obj in provider.products.all()]
        payload = {
            'title': title,
            'contact': provider.contact.pk,
            'products': products,
        }

        response = auth_client.post(path=url, data=payload, content_type='application/json')

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['title'] == title
        assert response.data['products'] == products
        assert response.data['level'] == provider.level
        assert response.data['id'] != provider.pk
        assert response.data['at_created'] != provider.at_created

    def test_create_provider_already_exists_title(self, auth_client, provider_level_0):
        provider = provider_level_0
        url = reverse('provider-list')

        title = provider.title
        payload = {
            'title': title,
            'contact': provider.contact.pk,
        }

        response = auth_client.post(path=url, data=payload, content_type='application/json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_list_provider_ok(self, auth_client, list_providers):
        url = reverse('provider-list')

        response = auth_client.get(path=url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == ProviderSerializer(list_providers, many=True).data

    def test_get_filtered_list_provider_ok(self, auth_client, list_providers, provider_factory):
        url = reverse('provider-list')

        size = 3
        country = 'zxcvbnmas'
        providers = provider_factory.create_batch(size=size, contact__country=country)

        response = auth_client.get(url, {'country': country})

        assert response.status_code == status.HTTP_200_OK
        assert response.data == ProviderSerializer(providers, many=True).data

    def test_get_single_provider_ok(self, auth_client, provider_level_1):
        provider = provider_level_1
        url = reverse('provider-detail', kwargs={'pk': provider.pk})

        response = auth_client.get(path=url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data == ProviderSerializer(provider).data

    def test_get_single_provider_with_debt(self, auth_client, provider_level_2_with_debt):
        provider = provider_level_2_with_debt
        url = reverse('provider-detail', kwargs={'pk': provider.pk})

        response = auth_client.get(path=url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['debt'] == provider.debt

    def test_update_provider_ok(self, auth_client, provider_level_0):
        provider = provider_level_0
        url = reverse('provider-detail', kwargs={'pk': provider.pk})

        title = 'updated title'
        payload = {
            'title': title,
        }

        response = auth_client.patch(path=url, data=payload, content_type='application/json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == title

    def test_update_provider_debt_denied(self, auth_client, provider_level_2_with_debt):
        provider = provider_level_2_with_debt
        url = reverse('provider-detail', kwargs={'pk': provider.pk})

        payload = {
            'debt': '0'
        }

        response = auth_client.patch(path=url, data=payload, content_type='application/json')

        assert response.status_code == status.HTTP_200_OK
        assert response.data['debt'] == provider.debt
        assert response.data['debt'] != '0.00'

    def test_update_provider_already_exists_title(self, auth_client, provider_level_0, list_providers):
        provider = provider_level_0
        url = reverse('provider-detail', kwargs={'pk': provider.pk})

        title = list_providers[0].title
        payload = {
            'title': title,
        }

        response = auth_client.put(path=url, data=payload, content_type='application/json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert provider.title != title

    def test_delete_provider_ok(self, auth_client, provider_level_0):
        provider = provider_level_0
        url = reverse('provider-detail', kwargs={'pk': provider.pk})

        response = auth_client.delete(path=url, content_type='application/json')

        assert response.status_code == status.HTTP_204_NO_CONTENT
