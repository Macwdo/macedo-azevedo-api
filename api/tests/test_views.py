from django.test import RequestFactory, TestCase

from api.views import OwnedByLawFirmGenericViewSet
from authentication.models import User
from authentication.tests.factories import UserFactory
from lawsuits.models.customer.models import Customer
from lawsuits.models.customer.tests.factories import CustomerFactory


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

        customer_1 = CustomerFactory(lawfirm__name="Lawfirm 1")
        customer_2 = CustomerFactory(lawfirm__name="Lawfirm 2")

        user.current_lawfirm = customer_1.lawfirm
        user.save()

        viewset.queryset = Customer.objects.all()  # type: ignore
        assert viewset.queryset.count() == 2

        request = RequestFactory()
        request.user = user  # type: ignore
        viewset.request = request  # type: ignore
        queryset = viewset.get_queryset()

        assert viewset.queryset.count() == 1
        assert viewset.queryset.first() == customer_1
