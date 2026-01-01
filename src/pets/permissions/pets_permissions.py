from rest_framework.permissions import BasePermission

METHOD_PERMISSION_MAP = {
    """Mapping of HTTP methods to required permissions."""
    "GET": "pets.get",
    "POST": "pets.create",
    "PUT": "pets.update",
    "PATCH": "pets.update",
    "DELETE": "pets.delete",
}


class PetsPermission(BasePermission):
    """
    Permissions control class for pet-related API operations.
    """

    message = "You do not have permission to perform this action."

    def has_permission(self, request, _):
        """
        Check if the user has the required permission for the HTTP method.
        """
        token = request.auth

        if not token:
            return False

        permissions = token.get("permissions", [])

        required = METHOD_PERMISSION_MAP.get(request.method)
        return required in permissions
