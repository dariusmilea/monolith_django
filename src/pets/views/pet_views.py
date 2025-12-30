from rest_framework import generics
from pets.permissions import PetsPermission
from pets.models import PetModel
from pets.serializers import PetSerializer


class PetsListView(generics.ListCreateAPIView):
    queryset = PetModel.objects.all()
    serializer_class = PetSerializer

    permission_classes = [
        PetsPermission,
    ]


class PetUpdateDestroyRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PetModel.objects.all()
    serializer_class = PetSerializer

    permission_classes = [
        PetsPermission,
    ]
