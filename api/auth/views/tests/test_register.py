from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authentication.models import User
from lawfirm.models import Account


class RegisterAPIViewTests(APITestCase):
    maxDiff = None

    def test_create_user_with_invalid_data(self):
        url = reverse("api:auth:register")
        response = self.client.post(url)

        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_create_user_with_valid_data(self):
        url = reverse("api:auth:register")
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@mail.com",
            "password": "password",
            "confirm_password": "password",
            "phone": {
                "number": "999999999",
                "ddi": "55",
                "ddd": "21",
            },
        }

        response = self.client.post(url, data=data)
        assert response.status_code == status.HTTP_201_CREATED

        user = User.objects.get(
            first_name="John",
            last_name="Doe",
            email="johndoe@mail.com",
        )
        Account.objects.get(
            owner=user,
            phone_number="999999999",
            phone_ddi="55",
            phone_ddd="21",
        )

        self.assertDictEqual(
            response.json(),
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "johndoe@mail.com",
                "password": "password",
                "confirm_password": "password",
                "phone": {
                    "number": "999999999",
                    "ddi": "55",
                    "ddd": "21",
                },
            },
        )
