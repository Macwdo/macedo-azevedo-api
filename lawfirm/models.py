from django.db import models

from common.models import Address, BaseModel, Email, Phone
from utils.user import get_user_model

user_model = get_user_model()


class Account(BaseModel):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(user_model, on_delete=models.PROTECT)


class Company(BaseModel):
    social_reason = models.CharField(max_length=100)
    social_name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class CompanyContacts(BaseModel):
    class Meta:
        unique_together = ["company", "main"]

    name = models.CharField(max_length=100)

    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    main = models.BooleanField(default=False)


class LawFirm(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField()

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class LawFirmUser(BaseModel):
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    lawfirm = models.ForeignKey(LawFirm, on_delete=models.CASCADE)


class OwnedByLawFirmQuerySet(models.QuerySet):
    def filter_by_lawfirm(self, lawfirm: LawFirm):
        return self.filter(lawfirm=lawfirm)


class OwnedByLawFirmManager(models.Manager):
    def get_queryset(self):
        return OwnedByLawFirmQuerySet(self.model, using=self._db)


class OwnedByLawFirm(BaseModel):
    class Meta:
        abstract = True

    lawfirm = models.ForeignKey(LawFirm, on_delete=models.CASCADE)
    objects = OwnedByLawFirmManager()
