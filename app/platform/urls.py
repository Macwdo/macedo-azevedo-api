from django.urls import path

from app.platform.views import home

app_name = "platform"

urlpatterns = [
    path("", home, name="home"),
]
