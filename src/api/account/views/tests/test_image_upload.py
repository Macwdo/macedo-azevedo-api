from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from authentication.models import User
from lawfirm.models import Account

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.memory.InMemoryStorage",
    },
}


@override_settings(STORAGES=STORAGES)
class AccountImageUploadViewTests(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email="john@email.com")
        self.account = Account.objects.create(
            owner=self.user,
            phone_number="1234567890",
            phone_ddd="11",
            phone_ddi="55",
        )
        self.client.force_authenticate(self.user)  # type: ignore

    def test_upload_image(self) -> None:
        url = reverse("api:account:image-upload")

        image = SimpleUploadedFile(content=b"file_content", name="file.txt")
        data = {
            "image": image,
        }

        response = self.client.post(url, data, format="multipart")

        assert response.status_code == status.HTTP_200_OK
        assert self.account.image.file.read() == b"file_content"
