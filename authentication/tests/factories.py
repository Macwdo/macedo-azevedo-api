import factory
import faker

from utils.user import get_user_model

_faker = faker.Faker("pt_BR")

user_model = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = user_model

    first_name = factory.LazyAttribute(lambda _: _faker.first_name())
    last_name = factory.LazyAttribute(lambda _: _faker.last_name())

    email = factory.LazyAttribute(lambda _: _faker.email())
    account = factory.SubFactory("lawfirm.tests.factories.AccountFactory")
    current_lawfirm = factory.SubFactory("lawfirm.tests.factories.LawFirmFactory")

    @factory.post_generation
    def deleted_by(self, created, extracted, **kwargs):
        self.deleted_by = extracted
        if not created:
            return

        self.deleted_by = extracted
        self.save()
