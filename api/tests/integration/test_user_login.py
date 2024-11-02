from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserRegisterAndLoginTestCase(APITestCase):
    maxDiff = None

    def test_create_user_and_login_then_get_me(self):
        """
        1. Create a user
        2. Login the user
        3. Me endpoint should return the user details

        """

        # Create a user
        register_url = reverse("api:auth:register")
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

        response = self.client.post(register_url, data=data)
        assert response.status_code == status.HTTP_201_CREATED

        # Login the user
        token_url = reverse("api:auth:token")
        data = {
            "email": "johndoe@mail.com",
            "password": "password",
        }

        response = self.client.post(token_url, data=data)
        assert response.status_code == status.HTTP_200_OK

        # Me endpoint should return the user details
        token = response.json()["access"]
        me_url = reverse("api:auth:me")

        response = self.client.get(me_url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

        response = self.client.get(me_url, HTTP_AUTHORIZATION=f"Bearer {token}")
        assert response.status_code == status.HTTP_200_OK
