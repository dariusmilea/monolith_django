from django.db import models
import uuid


class UserModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    permissions = models.JSONField(default=dict)
    is_staff = models.BooleanField(default=False)
    password_hash = models.CharField(max_length=255)

    def __str__(self):
        return self.email
