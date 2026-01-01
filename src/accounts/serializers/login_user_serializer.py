from rest_framework import serializers
from accounts.models import UserModel
from accounts.services import verify_password


class LoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user = UserModel.objects.get(email=data["email"])
        except UserModel.DoesNotExist:
            raise serializers.ValidationError("Invalid credentials")

        if not verify_password(user, data["password"]):
            raise serializers.ValidationError("Invalid credentials")

        if not user.is_active:
            raise serializers.ValidationError("User is inactive")

        data["user"] = user
        return data
