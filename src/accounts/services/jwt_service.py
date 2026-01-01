from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings
from datetime import datetime, timezone


def create_access_token(user):
    """
    Create a JWT access token for the given user.

    We use the rest_framework_simplejwt TokenBackend to encode the token for a more caveman implementation.
    The token contains the user ID as 'sub', user permissions.
    """
    backend = TokenBackend(
        algorithm=settings.SIMPLE_JWT["ALGORITHM"],
        signing_key=settings.SIMPLE_JWT["SIGNING_KEY"],
    )

    payload = {
        "sub": str(user.id),
        "permissions": user.permissions,
        "exp": datetime.now(tz=timezone.utc) + settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
        "iat": datetime.now(tz=timezone.utc),
        "type": "access",
    }

    return backend.encode(payload)
