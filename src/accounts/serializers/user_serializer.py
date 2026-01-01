from rest_framework import serializers
from accounts.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    """
    For admins only - Serializer for user API operations.
    """

    class Meta:
        model = UserModel
        fields = [
            "id",
            "email",
            "is_active",
            "is_staff",
            "permissions",
            "created_at",
            "last_updated_at",
        ]
