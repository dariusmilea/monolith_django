from rest_framework import generics
from ..models.pet_model import PetModel
from ..serializers.pet_serializer import PetSerializer


class PetsListView(generics.ListCreateAPIView):
    queryset = PetModel.objects.all()
    serializer_class = PetSerializer


class PetUpdateDestroyRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PetModel.objects.all()
    serializer_class = PetSerializer
