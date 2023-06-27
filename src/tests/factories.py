import factory
from django.contrib.auth.hashers import make_password


TEST_EMPLOYEE_PASSWORD = 'password12345'


class EmployeeFactory(factory.django.DjangoModelFactory):
    """Employee factory."""
    class Meta:
        model = 'employees.Employee'

    username = factory.Sequence(lambda n: f'test_user_{n}')
    password = make_password(TEST_EMPLOYEE_PASSWORD)
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class ContactFactory(factory.django.DjangoModelFactory):
    """Contact factory."""
    class Meta:
        model = 'chain_store.Contact'

    email = factory.Faker('email')
    country = factory.Faker('country')
    city = factory.Faker('city')
    street = factory.Faker('street_name')
    building_number = factory.Faker('building_number')


class ProductFactory(factory.django.DjangoModelFactory):
    """Product factory."""
    class Meta:
        model = 'chain_store.Product'

    title = factory.Sequence(lambda n: f'test product {n}')
    model = factory.Sequence(lambda n: n)
    release_date = factory.Faker('date')


class ProviderFactory(factory.django.DjangoModelFactory):
    """
    Provider factory.

    method products:
        implementation many to many related
    """
    class Meta:
        model = 'chain_store.Provider'

    title = factory.Faker('company')
    contact = factory.SubFactory(ContactFactory)

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for product in extracted:
                self.products.add(product)
