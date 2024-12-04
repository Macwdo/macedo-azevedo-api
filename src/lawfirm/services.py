from authentication.models import User
from common.models import File
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


def upload_account_image(
    *,
    account: Account,
    image,
) -> File | None:
    file = File(
        file=image,
        source=File.Source.ACCOUNT_IMAGE,
    )
    file.full_clean()
    file.save()

    if account.image:
        account.image.delete()

    account.image = file
    account.full_clean()

    account.save()

    return account.image
