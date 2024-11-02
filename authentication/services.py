from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import transaction

from api.exceptions import InternalException
from authentication.models import User
from common.services import create_phone
from lawfirm.services import create_account


@transaction.atomic
def create_user(
    *,
    first_name: str,
    last_name: str,
    email: str,
    password: str,
    phone_number: str,
    phone_ddi: str,
    phone_ddd: str,
) -> User:
    user = User.objects.create_user(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
    )  # type: ignore
    user.save()

    create_account(
        owner=user,
        phone_number=phone_number,
        phone_ddi=phone_ddi,
        phone_ddd=phone_ddd,
    )
    user.refresh_from_db()

    return user
