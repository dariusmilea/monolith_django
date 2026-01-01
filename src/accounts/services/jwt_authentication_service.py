from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings

from accounts.models import UserModel


class JWTAuthenticationService(BaseAuthentication):
    """
    API Authentication class using JWT tokens.
    """

    keyword = "Bearer"

    def authenticate(self, request):
        """
        Authenticate the user using a JWT token.

        It uses the rest_framework_simplejwt TokenBackend to decode and verify the token.
        Based on the settings defined in settings.SIMPLE_JWT.
        It also makes sure the user exists and is active.
        """
        header = request.headers.get("Authorization")
        if not header or not header.startswith(self.keyword + " "):
            return None

        raw_token = header.split(" ", 1)[1]

        backend = TokenBackend(
            algorithm=settings.SIMPLE_JWT["ALGORITHM"],
            signing_key=settings.SIMPLE_JWT["SIGNING_KEY"],
        )

        try:
            payload = backend.decode(raw_token, verify=True)
        except Exception:
            raise AuthenticationFailed("Invalid or expired token")

        user_id = payload.get("sub")
        if not user_id:
            raise AuthenticationFailed("Invalid token payload")

        try:
            user = UserModel.objects.get(id=user_id, is_active=True)
        except UserModel.DoesNotExist:
            raise AuthenticationFailed("Invalid token payload")

        return (user, payload)
