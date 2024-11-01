from authentication.models import User
from common.models import Phone
from lawfirm.models import Account


def create_account(
    *,
    owner: User,
    phone_number: str,
    phone_ddi: str,
    phone_ddd: str,
) -> Account:
    account = Account(
        owner=owner,
        phone_number=phone_number,
        phone_ddi=phone_ddi,
        phone_ddd=phone_ddd,
    )
    account.full_clean()
    account.save()

    return account
