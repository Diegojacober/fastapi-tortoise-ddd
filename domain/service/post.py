from pydantic import BaseModel
from adapter.post import PostTortoiseAdapter
from domain.entities.post import Post

class PostService(BaseModel):

    adapter: PostTortoiseAdapter

    async def list(self):
        return await self.adapter.list()

    async def create(self, post: Post):
        return await self.adapter.create(post)

    async def get(self, post_id: int):
        return await self.adapter.get(post_id)

    async def publish(self, post_id: int):
        return await self.adapter.publish(post_id)