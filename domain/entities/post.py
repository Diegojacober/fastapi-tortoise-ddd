from pydantic import Field

from .dto.postDto import PostDto
from .enums.post_status import PostStatus

class Post(PostDto):
    status: PostStatus = Field(default=PostStatus.DRAFT)