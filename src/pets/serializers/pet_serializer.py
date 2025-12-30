from rest_framework import serializers
from pets.models import PetModel


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetModel
        fields = ["id", "name", "age", "type", "created_at", "last_updated_at"]
