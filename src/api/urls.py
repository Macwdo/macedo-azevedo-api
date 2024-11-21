from django.urls import URLResolver

from api.account.urls import urlpatterns as account_urlpatterns
from api.auth.urls import urlpatterns as auth_urlpatterns

app_name = "api"

urlpatterns: list[URLResolver] = []
urlpatterns += auth_urlpatterns
urlpatterns += account_urlpatterns
