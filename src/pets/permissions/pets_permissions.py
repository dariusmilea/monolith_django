from rest_framework.permissions import BasePermission


class PetsPermission(BasePermission):
    """
    Permissions control class for pet-related API operations.
    """

    method_permission_map = {
        "GET": "pets.get",
        "POST": "pets.create",
        "PUT": "pets.update",
        "PATCH": "pets.update",
        "DELETE": "pets.delete",
    }
    message = "You do not have permission to perform this action."

    def has_permission(self, request, _):
        """
        Check if the user has the required permission for the HTTP method.
        """
        token = request.auth

        if not token:
            return False

        permissions = token.get("permissions", [])

        required = self.method_permission_map.get(request.method)
        return required in permissions
