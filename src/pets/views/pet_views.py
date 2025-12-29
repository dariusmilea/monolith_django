from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from ..permissions.pets_permission import PetsPermission
from ..models.pet_model import PetModel
from ..serializers.pet_serializer import PetSerializer


class PetsListView(generics.ListCreateAPIView):
    queryset = PetModel.objects.all()
    serializer_class = PetSerializer

    permission_classes = [
        IsAuthenticated,
        PetsPermission,
    ]


class PetUpdateDestroyRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PetModel.objects.all()
    serializer_class = PetSerializer

    permission_classes = [
        IsAuthenticated,
        PetsPermission,
    ]
