from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings
from datetime import datetime, timezone


def create_access_token(user):
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
