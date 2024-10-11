from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DocumentType(models.Model):
    name = models.CharField(max_length=255)

    @staticmethod
    def get_default() -> "DocumentType":
        default_document_type, _ = DocumentType.objects.get_or_create(
            name="Not defined"
        )
        return default_document_type


class Files(models.Model):
    file = models.FileField()
    description = models.CharField(max_length=255)
