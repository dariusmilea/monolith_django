from rest_framework.permissions import BasePermission

METHOD_PERMISSION_MAP = {
    "GET": "pets.get",
    "POST": "pets.create",
    "PUT": "pets.update",
    "PATCH": "pets.update",
    "DELETE": "pets.delete",
}


class PetsPermission(BasePermission):
    message = "You do not have permission to perform this action."

    def has_permission(self, request, _):
        token = request.auth

        print("Request Auth Token:", request.headers)

        if not token:
            return False

        permissions = token.get("permissions", [])

        required = METHOD_PERMISSION_MAP.get(request.method)
        return required in permissions
