from django.urls import URLResolver

from api.auth.urls import urlpatterns as auth_urlpatterns

app_name = "api"

urlpatterns: list[URLResolver] = []
urlpatterns += auth_urlpatterns
