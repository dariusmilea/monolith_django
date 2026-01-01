from django.contrib.auth.hashers import make_password, check_password
from accounts.models import UserModel


def create_user(email: str, password: str):
    """
    Create and return a new user with the given email and password.
    """
    return UserModel.objects.create(
        email=email,
        password_hash=make_password(password),
    )


def verify_password(user: UserModel, raw_password: str) -> bool:
    """
    Verify if the provided raw_password matches the user's stored password hash.
    """
    return check_password(raw_password, user.password_hash)
