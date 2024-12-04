import contextlib
from typing import TYPE_CHECKING

import pytest
from django.db import IntegrityError
from django.test import TestCase

from authentication.models import User
from lawfirm.models import Account

if TYPE_CHECKING:
    from authentication.manager import CustomUserManager


class UsersManagersTests(TestCase):
    def setUp(self) -> None:
        self.user_manager: CustomUserManager = User.objects  # type: ignore

    def test_create_user(self) -> None:
        user = self.user_manager.create_user(
            email="normal@user.com",
            password="password",
        )
        Account.objects.create(owner=user)
        assert user.email == "normal@user.com"
        assert user.is_active
        assert not user.is_staff
        assert not user.is_superuser
        try:  # noqa: SIM105
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            assert user.username is None
        except AttributeError:
            pass

        with pytest.raises(ValueError):
            self.user_manager.create_user(
                email=None,
                password="password",
            )

        with pytest.raises(ValueError):
            self.user_manager.create_user(
                email="",
                password="password",
            )

        with pytest.raises(ValueError):
            self.user_manager.create_user(
                email="",
                password="password",
            )

    def test_create_superuser(self) -> None:
        admin_user = self.user_manager.create_superuser(
            email="super@user.com",
            password="password",
        )
        Account.objects.create(owner=admin_user)

        assert admin_user.email == "super@user.com"
        assert admin_user.is_active
        assert admin_user.is_staff
        assert admin_user.is_superuser

        with contextlib.suppress(AttributeError):
            assert admin_user.username is None

        with pytest.raises(IntegrityError):
            extra_fields = dict(is_superuser=False)
            self.user_manager.create_user(
                email="super@user.com",
                password="password",
                extra_fields=extra_fields,
            )
