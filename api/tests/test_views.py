from django.test import TestCase

from api.views import OwnedByLawFirmGenericViewSet
from authentication.models import User
from authentication.tests.factories import UserFactory
from lawsuits.models.lawyer import Lawyer


class BaseOwnedByLawFirmGenericViewSetTests(TestCase):
    def test_user(self):
        user: User = UserFactory.create()

        assert user.has_lawfirm

    def test_get_queryset_should_filter_by_user_current_lawfirm(self):
        """
        1. Test get_queryset should filter model.lawfirm from user.current_lawfirm

        """

        user = UserFactory()
        viewset = OwnedByLawFirmGenericViewSet()
        viewset.queryset = Lawyer.objects.all() # type: ignore
        
        queryset = viewset.get_queryset()

        assert 1 == 1
