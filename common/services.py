from authentication.models import User
from common.models import Phone
from lawfirm.models import Account


def create_phone(*, number: str, ddi: str, ddd: str) -> Phone:
    phone = Phone(
        number=number,
        ddi=ddi,
        ddd=ddd,
    )
    phone.full_clean()
    phone.save()

    return phone
