from django.test import RequestFactory, TestCase

from api.views import OwnedByLawFirmGenericViewSet
from authentication.models import User
from authentication.tests.factories import UserFactory
from lawsuits.models.customer.models import Customer
from lawsuits.models.customer.tests.factories import CustomerFactory


class BaseOwnedByLawFirmGenericViewSetTests(TestCase):
    def test_user(self):
        user: User = UserFactory.build(current_lawfirm__name="Lawfirm 1")

        assert user.has_lawfirm

    def test_get_queryset_should_filter_by_user_current_lawfirm(self):
        """
        This test should filter the queryset by the user's current lawfirmk

        """

        user = UserFactory()
        viewset = OwnedByLawFirmGenericViewSet()

        customer_1 = CustomerFactory(lawfirm__name="Lawfirm 1")
        customer_2 = CustomerFactory(lawfirm__name="Lawfirm 2")

        user.current_lawfirm = customer_1.lawfirm
        user.save()

        viewset.queryset = Customer.objects.all()  # type: ignore
        self.assertEqual(viewset.queryset.count(), 2)  # type: ignore

        request = RequestFactory()
        request.user = user  # type: ignore
        viewset.request = request  # type: ignore
        queryset = viewset.get_queryset()

        self.assertEqual(queryset.count(), 1)
        self.assertEqual(queryset[0], customer_1)
