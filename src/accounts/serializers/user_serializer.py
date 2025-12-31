from rest_framework import serializers
from accounts.models import UserModel


class UserSerializer(serializers.ModelSerializer):
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
