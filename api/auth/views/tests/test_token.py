from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authentication.models import User
from authentication.tests.factories import UserFactory
from lawfirm.tests.factories import AccountFactory


class TokenObtainPairTests(APITestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.user = UserFactory(  # type: ignore
            first_name="John",
            last_name="Doe",
            email="johndoe@mail.com",
        )
        self.password = "STRONGPASSWORD123@"
        self.user.set_password(self.password)
        self.user.save()

    def test_post_should_return_jwt_token_(self):
        url = reverse("api:auth:token-obtain-pair")
        data = {"email": self.user.email, "password": self.password}

        response = self.client.post(url, data)

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["refresh"] is not None
        assert response.json()["access"] is not None
