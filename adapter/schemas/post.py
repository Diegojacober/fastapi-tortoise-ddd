from tortoise.models import Model
from tortoise import fields
from domain.entities.post import PostStatus

class PostModel(Model):
    id = fields.IntField(pk=True)
    status = fields.CharEnumField(enum_type=PostStatus, default=PostStatus.DRAFT)
    title = fields.TextField()
    content = fields.TextField()

    def __str__(self):
        return self.title