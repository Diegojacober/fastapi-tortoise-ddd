from pydantic import Field
from enum import Enum
from pydantic import BaseModel

class PostStatus(str, Enum):
    PUBLISHED = "published"
    DRAFT = "draft"

class PostDto(BaseModel):
    title: str
    content: str

class Post(PostDto):
    status: PostStatus = Field(default=PostStatus.DRAFT)