from django.test import RequestFactory, TestCase, tag

from api.views import OwnedByLawFirmGenericViewSet
from authentication.models import User
from lawfirm.models import Account, LawFirm, LawFirmOwner
from lawsuits.models.customer.models import Customer


class BaseOwnedByLawFirmGenericViewSetTests(TestCase):
    def test_user(self):
        user: User = User(current_lawfirm=LawFirm())

        assert user.has_lawfirm

    def test_get_queryset_should_filter_by_user_current_lawfirm(self):
        """
        This test should filter the queryset by the user's current lawfirm

        """

        user = User.objects.create()
        user_current_lawfirm = LawFirm.objects.create(
            name="Lawfirm 1",
            owner=LawFirmOwner.objects.create(),
        )
        user.current_lawfirm = user_current_lawfirm  # type: ignore
        user.save()

        viewset = OwnedByLawFirmGenericViewSet()
        another_lawfirm = LawFirm.objects.create(
            name="Lawfirm 2",
            owner=LawFirmOwner.objects.create(),
        )

        customer_from_user_current_lawfirm = Customer.objects.create(
            lawfirm=user_current_lawfirm,
        )
        Customer.objects.create(lawfirm=another_lawfirm)

        user.save()

        viewset.queryset = Customer.objects.all()  # type: ignore
        self.assertEqual(viewset.queryset.count(), 2)  # type: ignore

        request = RequestFactory()
        request.user = user  # type: ignore
        viewset.request = request  # type: ignore
        queryset = viewset.get_queryset()

        self.assertEqual(queryset.count(), 1)
        self.assertEqual(queryset[0], customer_from_user_current_lawfirm)
