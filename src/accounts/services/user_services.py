from accounts.models.user_model import UserModel


def user_has_permission(user: UserModel, permission: str) -> bool:
    """
    Check if a user has a specific permission based on their roles.

    Args:
        user (UserModel): The user to check.
        permission (str): The permission to check for.
    """

    if not user or user.is_authenticated:
        return False

    role_permissions = set()

    for role in user.roles.all():
        role_permissions.update(role.permissions.keys())

    return permission in role_permissions
