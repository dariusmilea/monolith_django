# accounts/serializers.py
from rest_framework import serializers
from accounts.services import create_user


class RegisterSerializer(serializers.Serializer):
    """
    Serializer for user registration.
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        return create_user(
            email=validated_data["email"],
            password=validated_data["password"],
        )
