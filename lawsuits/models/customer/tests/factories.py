import factory
import faker

from lawsuits.models.customer.models import Customer

_faker = faker.Faker("pt_br")


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    name = factory.LazyAttribute(lambda _: _faker.name())
    birth_date = factory.LazyAttribute(lambda _: _faker.date_time())
    lawfirm = factory.SubFactory("lawfirm.tests.factories.LawFirmFactory")
