from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.serializers import LoginSerializer
from accounts.services import create_access_token


class LoginView(APIView):
    #TODO: Add docstrings
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        token = create_access_token(user)

        return Response(
            {
                "access": token,
            }
        )
