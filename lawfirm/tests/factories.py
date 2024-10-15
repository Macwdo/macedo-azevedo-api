import factory
import faker

from authentication.tests.factories import UserFactory
from common.tests.factories import AddressFactory
from lawfirm.models import Account, Company, LawFirm, LawFirmUser

_faker = faker.Faker("pt_BR")


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    name = factory.LazyAttribute(lambda _: _faker.company())
    user = factory.SubFactory("authentication.tests.factories.UserFactory")


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    social_reason = factory.LazyAttribute(lambda _: _faker.company())
    social_name = factory.LazyAttribute(lambda _: _faker.company())
    cnpj = factory.LazyAttribute(lambda _: _faker.cnpj())

    account = factory.SubFactory(AccountFactory)
    address = factory.SubFactory(AddressFactory)
    main = False


class LawFirmFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LawFirm

    name = factory.LazyAttribute(lambda _: _faker.company())
    image = factory.django.ImageField(color="blue")

    account = factory.SubFactory(AccountFactory)
    company = factory.SubFactory(CompanyFactory)


class LawFirmUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = LawFirmUser

    user = factory.SubFactory(UserFactory)
    lawfirm = factory.SubFactory(LawFirmFactory)
