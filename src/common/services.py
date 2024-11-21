from common.models import Phone


def create_phone(*, number: str, ddi: str, ddd: str) -> Phone:
    phone = Phone(
        number=number,
        ddi=ddi,
        ddd=ddd,
    )
    phone.full_clean()
    phone.save()

    return phone
