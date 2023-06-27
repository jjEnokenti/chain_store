import pytest

from tests import factories


@pytest.fixture
def auth_client(client, employee):
    client.force_login(employee)
    return client


@pytest.fixture
def employee(db):
    return factories.EmployeeFactory.create()


@pytest.fixture
def list_providers():
    return factories.ProviderFactory.create_batch(size=5)


@pytest.fixture
def provider_factory():
    return factories.ProviderFactory


@pytest.fixture
def provider_level_0():
    return factories.ProviderFactory.create(
        provider=None,
        products=(factories.ProductFactory.create_batch(size=5))
    )


@pytest.fixture
def provider_level_1(provider_level_0):
    return factories.ProviderFactory.create(
        provider=provider_level_0,
        products=(factories.ProductFactory.create_batch(size=5))
    )


@pytest.fixture
def provider_level_2_with_debt(provider_level_1):
    return factories.ProviderFactory.create(
        level=2,
        debt='123.32',
        provider=provider_level_1,
        products=(factories.ProductFactory.create_batch(size=5))
    )
