from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.manager import CustomUserManager
from common.models import BaseModel

if TYPE_CHECKING:
    from lawfirm.models import Account


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

    objects = CustomUserManager()  # type: ignore
    # TODO: Add clean validation with account and creation

    @property
    def has_lawfirm(self) -> bool:
        return self.current_lawfirm is not None

    @property
    def account(self) -> Account | None:
        return getattr(self, "user_account", None)
