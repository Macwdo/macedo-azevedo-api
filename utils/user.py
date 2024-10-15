from authentication.models import User


def get_user_model() -> type[User]:
    """
    Return the User model that is active in this project.
    """
    from django.contrib.auth import get_user_model

    return get_user_model()  # type: ignore
