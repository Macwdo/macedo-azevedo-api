from django.contrib.auth.models import AnonymousUser
from rest_framework.request import HttpRequest

from authentication.models import User
from lawfirm.models import LawFirm


class UserWithLawFirm(User):
    current_lawfirm: LawFirm


class UserWithLawFirmRequest(HttpRequest):
    user: UserWithLawFirm | AnonymousUser
