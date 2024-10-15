from django.db import models

from common.models import Address, BaseModel, CpfField, DocumentType, Files, Phone
from lawsuits.models import Lawyer


class Customer(BaseModel):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()


class CustomerReferred(BaseModel):
    class Meta:
        abstract = True
        unique_together = ("customer", "reffered_by")


class CustomerReferredByCustomer(CustomerReferred):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reffered_by = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="referred_customers"
    )


class CustomerReferredByLawyer(CustomerReferred):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    reffered_by = models.ForeignKey(
        Lawyer, on_delete=models.CASCADE, related_name="referred_customers"
    )


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
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class PhysicalPersonCustomer(BaseModel):
    # TODO: Test it
    cpf = CpfField()
    rg = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class JuridicalPersonCustomer(BaseModel):
    social_reason = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    birth_date = models.DateField()
