from django.urls import path
from .views.pet_views import PetsListView, PetUpdateDestroyRetrieveView

urlpatterns = [
    path("", PetsListView.as_view(), name="pets-list-create-view"),
    path("/<uuid:pk>/", PetUpdateDestroyRetrieveView.as_view(), name="pet-update-destroy-retrieve-view"),
]
