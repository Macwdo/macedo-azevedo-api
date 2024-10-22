from django.contrib.auth.models import AbstractUser
from django.db import models

from common.models import BaseModel

# Create your models here.


class User(AbstractUser, BaseModel):
    email = models.EmailField(unique=True, db_index=True)
    current_lawfirm = models.OneToOneField(
        "lawfirm.LawFirm",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    account = models.OneToOneField(
        "lawfirm.Account",
        on_delete=models.PROTECT,
        null=False,
        blank=False,
    )
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
