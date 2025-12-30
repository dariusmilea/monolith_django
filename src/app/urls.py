from django.urls import path, include

urlpatterns = [
    path("api/pets/", include("pets.urls")),
    path("api/auth/", include("accounts.urls")),
]
