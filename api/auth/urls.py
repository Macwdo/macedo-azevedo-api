from django.urls import include, path
from django.urls.resolvers import URLResolver
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.auth.views import MeApiView, RegisterApiView

urlpatterns: list[URLResolver] = [
    path(
        "auth/",
        include(
            (
                [
                    path(
                        "token/",
                        TokenObtainPairView.as_view(),
                        name="token",
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
                    path(
                        "register/",
                        RegisterApiView.as_view(),
                        name="register",
                    ),
                ],
                "auth",
            ),
        ),
    ),
]
