from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.serializers import RegisterSerializer


class RegisterView(APIView):
    #TODO: Add docstrings
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                "id": user.id,
                "email": user.email,
                "created_at": user.created_at,
                "last_updated_at": user.last_updated_at,
            },
            status=status.HTTP_201_CREATED,
        )
