from django.urls import include, path
from django.urls.resolvers import URLResolver
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.auth.views.me import MeApiView

app_name = "auth"

urlpatterns: list[URLResolver] = [
    path(
        "auth/",
        include(
            (
                [
                    path(
                        "token/",
                        TokenObtainPairView.as_view(),
                        name="token-obtain-pair",
                    ),
                    path(
                        "token/refresh/",
                        TokenRefreshView.as_view(),
                        name="token-refresh",
                    ),
                    path(
                        "me/",
                        MeApiView.as_view(),
                        name="me",
                    ),
                ],
                "auth",
            )
        ),
    ),
]
