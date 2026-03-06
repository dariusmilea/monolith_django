from django.db import models
import uuid


class PetModel(models.Model):
    """
    DB Model representing a pet.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    age = models.IntegerField() #TODO: min = 0, max = maximul bazei de date
    type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.type}, {self.age} years old)"
