from django.db import models

from lawsuits.models.commons import BaseModel, DocumentType, Files
from lawsuits.models.lawyer import Lawyer
from lawsuits.models.phone import Phone


class CpfField(models.CharField): ...


class Customer(BaseModel):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()


class CustomerReferred(BaseModel):
    class Meta(BaseModel.Meta):
        abstract = True
        unique_together = ("customer", "referred")


class CustomerReferredFromCustomer(CustomerReferred):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="customer"
    )
    referred_customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="referred_customer"
    )


class CustomerReferredFromLawyer(CustomerReferred):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)


class CustomerDocument(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    document_type = models.ForeignKey(
        DocumentType, on_delete=models.SET_DEFAULT, default=DocumentType.get_default
    )
    referent = models.CharField(max_length=255, help_text="Referent to the document")
    description = models.CharField(max_length=255)


class CustomerDocumentFile(BaseModel):
    customer_document = models.ForeignKey(CustomerDocument, on_delete=models.CASCADE)
    file = models.ForeignKey(Files, on_delete=models.CASCADE)


class CustomerEmail(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    email = models.EmailField()


class CustomerPhone(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)


class CustomerAddress(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)


class PhysicalPersonCustomer(BaseModel):
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class JuridicalPersonCustomer(BaseModel):
    social_reason = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)