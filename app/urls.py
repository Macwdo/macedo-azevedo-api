from django.urls import include, path

urlpatterns = [
    path("auth/", include("app.auth.urls")),
    path("", include("app.platform.urls")),
]
