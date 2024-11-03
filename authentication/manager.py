from typing import TYPE_CHECKING

from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.password_validation import validate_password

if TYPE_CHECKING:
    from .models import User


class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        email: str,
        password: str,
        **extra_fields: dict[str, str],
    ) -> "User":
        if not email:
            msg = "The Email field must be set"
            raise ValueError(msg)

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        validate_password(password, user)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email: str,
        password: str | None = None,
        **extra_fields,
    ) -> "User":
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)
