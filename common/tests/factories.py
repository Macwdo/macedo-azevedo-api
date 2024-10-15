import factory
import faker

from common.models import Address, DocumentType, Email, Files, Phone

_faker = faker.Faker("pt_BR")


class DocumentTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DocumentType

    name = factory.LazyAttribute(lambda _: _faker.name())


class FilesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Files

    file = factory.django.FileField(filename="test.txt")
    description = factory.LazyAttribute(lambda _: _faker.text())


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    street = factory.LazyAttribute(lambda _: _faker.street_name())
    city = factory.LazyAttribute(lambda _: _faker.city())
    state = factory.LazyAttribute(lambda _: _faker.state())
    zip_code = factory.LazyAttribute(lambda _: _faker.zipcode())


class PhoneFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Phone

    ddi = factory.LazyAttribute(lambda _: _faker.country_calling_code())
    phone = factory.LazyAttribute(lambda _: _faker.numerify(text="#########"))
    ddd = factory.LazyAttribute(lambda _: _faker.numerify(text="##"))


class EmailFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Email

    email = factory.LazyAttribute(lambda _: _faker.email())
