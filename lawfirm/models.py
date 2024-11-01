from django.core.exceptions import ValidationError
from django.db import models

from common.models import Address, BaseModel, Email, Phone
from utils.user import get_user_model

user_model = get_user_model()


class Account(BaseModel):
    phone_number = models.CharField(max_length=20)
    phone_ddd = models.CharField(max_length=20)
    phone_ddi = models.CharField(max_length=20)
    owner = models.OneToOneField(
        user_model,
        on_delete=models.CASCADE,
        related_name="account",
    )


class Company(BaseModel):
    social_reason = models.CharField(max_length=255)
    social_name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=20)

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class CompanyContacts(BaseModel):
    name = models.CharField(max_length=255)

    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    main = models.BooleanField(default=False)

    def clean(self) -> None:
        if not self.main:
            return super().clean()

        has_main_contact = self.objects.filter(company=self.company, main=True).exists()
        if has_main_contact:
            raise ValidationError("Main contact already exists")

        return super().clean()


class LawFirm(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    owner = models.OneToOneField(
        "LawFirmOwner",
        on_delete=models.CASCADE,
    )


class LawFirmOwner(BaseModel):
    class LawFirmOwnerType(models.TextChoices):
        COMPANY = ("company", "Company")
        ACCOUNT = ("account", "Account")

    physical_person_owner = models.ForeignKey(
        "Account",
        on_delete=models.CASCADE,
        related_name="lawfirms",
        null=True,
        blank=True,
    )
    juridical_person_owner = models.ForeignKey(
        "Company",
        on_delete=models.CASCADE,
        related_name="lawfirms",
        null=True,
        blank=True,
    )

    @property
    def owner_type(self):
        has_juridical_person_owner = self.juridical_person_owner is not None
        has_physical_person_owner = self.physical_person_owner is not None

        if not (has_juridical_person_owner or has_physical_person_owner):
            raise ValidationError("LawFirmOwner was created without an owner")

        if has_juridical_person_owner:
            return self.LawFirmOwnerType.COMPANY

        return self.LawFirmOwnerType.ACCOUNT

    def clean(self) -> None:
        has_juridical_person_owner = self.juridical_person_owner is not None
        has_physical_person_owner = self.physical_person_owner is not None

        if not (has_physical_person_owner and has_juridical_person_owner):
            raise ValidationError("You need to set an owner to create a LawFirmOwner.")

        return super().clean()


class OwnedByLawFirmQuerySet(models.QuerySet):
    def filter_by_lawfirm(self, lawfirm: LawFirm):
        return self.filter(lawfirm=lawfirm)


class OwnedByLawFirmManager(models.Manager): ...


class OwnedByLawFirm(BaseModel):
    class Meta:
        abstract = True

    lawfirm = models.ForeignKey(
        LawFirm,
        on_delete=models.CASCADE,
        related_name="%(class)s_lawfirm",
    )
    objects = OwnedByLawFirmManager.from_queryset(OwnedByLawFirmQuerySet)()
