from django.urls import include, path

app_name = "app"

urlpatterns = [
    path("auth/", include("app.auth.urls")),
    path("", include("app.platform.urls")),
]
