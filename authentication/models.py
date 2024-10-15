from django.db import models
from django.contrib.auth.models import AbstractUser

from common.models import BaseModel


# Create your models here.


class User(AbstractUser, BaseModel):
    email = models.EmailField(unique=True, db_index=True)
    current_lawfirm = models.OneToOneField(
        "lawfirm.LawFirm", on_delete=models.SET_NULL, null=True, blank=True
    )
    lawfirms = models.ManyToManyField("lawfirm.LawFirmUser", related_name="users")

    deleted_at = models.DateTimeField(auto_now_add=True)
    deleted_by = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    @property
    def has_lawfirm(self):
        return self.current_lawfirm is not None
