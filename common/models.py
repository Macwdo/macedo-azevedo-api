from django.core.exceptions import ValidationError
from django.db import models


class CpfField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 11
        super().__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        self.validate_cpf(value)

    def validate_cpf(self, value):
        cpf = self.clean_cpf(value)
        if not self.is_valid_cpf(cpf):
            raise ValidationError("Invalid CPF")

    def clean_cpf(self, value):
        return "".join(filter(str.isdigit, value))

    def is_valid_cpf(self, cpf):
        if len(cpf) != 11:
            return False
        if cpf == cpf[::-1]:
            return False
        cpf_digits = list(map(int, cpf))
        first_digit = self.calculate_digit(cpf_digits[:9])
        second_digit = self.calculate_digit(cpf_digits[:10])
        return cpf_digits[9] == first_digit and cpf_digits[10] == second_digit

    def calculate_digit(self, digits):
        total = sum((i + 2) * digit for i, digit in enumerate(digits[::-1]))
        remainder = total % 11
        return (11 - remainder) % 10


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DocumentType(BaseModel):
    name = models.CharField(max_length=255)

    @staticmethod
    def get_default() -> "DocumentType":
        default_document_type, _ = DocumentType.objects.get_or_create(
            name="Not defined"
        )
        return default_document_type


class Files(BaseModel):
    file = models.FileField()
    description = models.CharField(max_length=255)


class Address(BaseModel):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)


class Phone(BaseModel):
    phone = models.CharField(max_length=20)
    ddi = models.CharField(max_length=5)
    ddd = models.CharField(max_length=5)


class Email(BaseModel):
    email = models.EmailField()
