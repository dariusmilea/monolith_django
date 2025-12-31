from rest_framework.permissions import BasePermission


class IsStaffUser(BasePermission):
    message = "Only staff users are allowed to perform this action."

    def has_permission(self, request, view):
        user = request.user

        if not user:
            return False

        # Prevent staff users from deleting their own accounts
        if request.method == "DELETE" and str(request.user.id) == view.kwargs.get("pk"):
            return False

        return bool(user.is_staff)
