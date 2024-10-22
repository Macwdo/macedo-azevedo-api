import factory
import faker

from authentication.tests.factories import UserFactory
from common.tests.factories import AddressFactory
from lawfirm.models import Account, Company, LawFirm, LawFirmOwner

_faker = faker.Faker("pt_BR")


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    name = factory.LazyAttribute(lambda _: _faker.company())


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    social_reason = factory.LazyAttribute(lambda _: _faker.company())
    social_name = factory.LazyAttribute(lambda _: _faker.company())
    cnpj = factory.LazyAttribute(lambda _: _faker.cnpj())

    account = factory.SubFactory(AccountFactory)
    address = factory.SubFactory(AddressFactory)


class LawFirmOwnerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LawFirmOwner

    juridical_person_owner = factory.SubFactory(CompanyFactory)
    physical_person_owner = factory.SubFactory(AccountFactory)


class LawFirmFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LawFirm

    name = factory.LazyAttribute(lambda _: _faker.company())
    image = factory.django.ImageField(color="blue")
    owner = factory.SubFactory(LawFirmOwnerFactory)
