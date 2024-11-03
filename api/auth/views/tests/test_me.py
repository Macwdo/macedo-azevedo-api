from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authentication.models import User


class MeApiViewTests(APITestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.url = reverse("api:auth:me")
        self.user = User(  # type: ignore
            first_name="John",
            last_name="Doe",
            email="johndoe@mail.com",
        )

    def test_get_me_unauthenticated_should_return_401(self) -> None:
        response = self.client.get(self.url)
        assert response.status_code, status.HTTP_401_UNAUTHORIZED

    def test_get_should_return_me_values(self) -> None:
        self.client.force_authenticate(user=self.user)  # type: ignore

        response = self.client.get(self.url)
        expected = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@mail.com",
        }

        assert response.status_code, status.HTTP_200_OK
        assert response.json(), expected
