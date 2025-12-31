# accounts/urls.py
from django.urls import path
from accounts.views import RegisterView, LoginView, UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("admin/users/", UserListCreateView.as_view()),
    path("admin/users/<uuid:pk>/", UserRetrieveUpdateDestroyView.as_view()),
]
