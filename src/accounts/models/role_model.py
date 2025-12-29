from django.db import models
from .user_model import UserModel
import uuid


class RoleModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    permissions = models.JSONField(default=dict, blank=True)

    users = models.ManyToManyField(
        UserModel,
        related_name="roles",
        blank=True,
    )

    def __str__(self):
        return self.name
