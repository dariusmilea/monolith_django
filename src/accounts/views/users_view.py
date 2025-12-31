from rest_framework import generics

from accounts.models import UserModel
from accounts.serializers import UserSerializer
from accounts.permissions import IsStaffUser


class UserListCreateView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsStaffUser]


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsStaffUser]
