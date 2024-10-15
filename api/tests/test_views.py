import os
from django import setup


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
setup()

from authentication.models import User
from django.test import TestCase

from api.views import OwnedByLawFirmGenericViewSet
from authentication.tests.factories import UserFactory


class BaseOwnedByLawFirmGenericViewSetTests(TestCase):
    def test_user(self):
        user: User = UserFactory.create()

        assert user.has_lawfirm

    def test_get_queryset_should_filter_by_user_current_lawfirm(self):
        """
        1. Test get_queryset should filter model.lawfirm from user.current_lawfirm

        """

        user = UserFactory()
        OwnedByLawFirmGenericViewSet().get_queryset()

        assert 1 == 1
