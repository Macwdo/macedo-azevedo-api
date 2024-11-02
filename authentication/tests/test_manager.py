from django.db import IntegrityError
from django.test import TestCase

from authentication.manager import CustomUserManager
from authentication.models import User
from lawfirm.models import Account


class UsersManagersTests(TestCase):
    def setUp(self):
        self.user_manager: CustomUserManager = User.objects  # type: ignore

    def test_create_user(self):
        user = self.user_manager.create_user(
            email="normal@user.com",
            password="password",
        )
        account = Account.objects.create(owner=user)
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        with self.assertRaises(ValueError):
            self.user_manager.create_user(
                email=None,
                password="password",
            )

        with self.assertRaises(ValueError):
            self.user_manager.create_user(
                email="",
                password="password",
            )

        with self.assertRaises(ValueError):
            self.user_manager.create_user(
                email="",
                password="password",
            )

    def test_create_superuser(self):
        admin_user = self.user_manager.create_superuser(
            email="super@user.com",
            password="password",
        )
        account = Account.objects.create(owner=admin_user)

        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        try:
            assert admin_user.username is None

        except AttributeError:
            pass

        with self.assertRaises(IntegrityError):
            self.user_manager.create_user(
                email="super@user.com",
                password="password",
                is_superuser=False,
            )
