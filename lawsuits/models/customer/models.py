from django.db import models

from common.models import Address, CpfField, DocumentType, Files, Phone
from lawfirm.models import OwnedByLawFirm


class Customer(OwnedByLawFirm):
    class Gender(models.TextChoices):
        MEN = ("men", "Men")
        WOMAN = ("woman", "Woman")
        NOT_INFORMED = ("not_informed", "Not informed")

    name = models.CharField(max_length=255)
    gender = models.CharField(choices=Gender, max_length=20)
    birth_date = models.DateField()
    reffered = models.OneToOneField(
        "CustomerReferred",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )


class CustomerReferred(OwnedByLawFirm):
    class Source(models.TextChoices):
        WEBSITE = ("website", "Website")
        SOCIAL_NETWORK = ("social_network", "Social Network")
        LAWYER_REFFER = ("lawyer_reffer", "Lawyer Reffer")
        CUSTOMER_REFFER = ("customer_reffer", "Customer Reffer")

    comment = models.TextField()
    customer_refer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="referred",
    )
    lawyer_refer = models.ForeignKey(
        "lawsuits.Lawyer",
        on_delete=models.CASCADE,
        related_name="referred",
    )
    source = models.CharField(choices=Source, max_length=50)


class CustomerDocument(OwnedByLawFirm):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    document_type = models.ForeignKey(
        DocumentType,
        on_delete=models.SET_DEFAULT,
        default=DocumentType.get_default,
    )


class CustomerDocumentFile(OwnedByLawFirm):
    customer_document = models.ForeignKey(CustomerDocument, on_delete=models.CASCADE)
    file = models.ForeignKey(Files, on_delete=models.CASCADE)


class CustomerEmail(OwnedByLawFirm):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    email = models.EmailField()


class CustomerPhone(OwnedByLawFirm):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)


class CustomerAddress(OwnedByLawFirm):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class PhysicalPersonCustomer(OwnedByLawFirm):
    # TODO: Test it
    cpf = models.CharField(max_length=20)
    rg = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class JuridicalPersonCustomer(OwnedByLawFirm):
    social_reason = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=25)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    birth_date = models.DateField()
