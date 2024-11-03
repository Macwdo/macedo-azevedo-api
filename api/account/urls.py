from django.urls import include, path
from django.urls.resolvers import URLResolver

from api.account.views.image_upload import AccountImageUploadView

urlpatterns: list[URLResolver] = [
    path(
        "account/",
        include(
            (
                [
                    path(
                        "image-upload/",
                        AccountImageUploadView.as_view(),
                        name="image-upload",
                    ),
                ],
                "account",
            ),
        ),
    ),
]
