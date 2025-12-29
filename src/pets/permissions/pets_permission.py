from rest_framework.permissions import BasePermission
from accounts.services.user_services import user_has_permission


METHOD_PERMISSION_MAP = {
    "GET": "pets.get",
    "POST": "pets.create",
    "PUT": "pets.update",
    "PATCH": "pets.update",
    "DELETE": "pets.delete",
}


class PetsPermission(BasePermission):
    def has_permission(self, request, view):
        required_perm = METHOD_PERMISSION_MAP.get(request.method)

        if not required_perm:
            return False

        return user_has_permission(request.user, required_perm)
