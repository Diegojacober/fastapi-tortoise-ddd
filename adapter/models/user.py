from tortoise.models import Model
from tortoise import fields
from uuid import uuid4

class UserModel(Model):
    id = fields.UUIDField(default=uuid4, pk=True)
    first_name = fields.CharField(max_length=255, null=False)
    last_name = fields.CharField(max_length=255, null=True)
    email = fields.CharField(max_length=255, unique=True, index=True, null=False)
    password = fields.CharField(max_length=255, null=False)
    active = fields.BooleanField(default=True)
    
    class Meta:
        table="users"
        description = "table for user in the system"
        # unique_together = (("first_name", "last_name", "email"))

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"