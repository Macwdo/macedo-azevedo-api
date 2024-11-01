from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.manager import CustomUserManager
from common.models import BaseModel


class User(AbstractUser, BaseModel):
    username = None
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    current_lawfirm = models.OneToOneField(
        "lawfirm.LawFirm",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    deleted_at = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    @property
    def has_lawfirm(self) -> bool:
        return self.current_lawfirm is not None
