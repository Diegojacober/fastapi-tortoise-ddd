from enum import Enum

class PostStatus(str, Enum):
    PUBLISHED = "published"
    DRAFT = "draft"