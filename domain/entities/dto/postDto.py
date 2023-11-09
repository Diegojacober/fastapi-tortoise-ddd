from pydantic import BaseModel

class PostDto(BaseModel):
    title: str
    content: str
