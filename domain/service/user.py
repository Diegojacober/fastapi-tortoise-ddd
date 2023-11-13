from pydantic import BaseModel
from adapter.user import UserTortoiseAdapter

class UserService(BaseModel):

    adapter: UserTortoiseAdapter

    async def listAll(self):
        return await self.adapter.listAll()

    async def create(self, post: Post):
        return await self.adapter.create(post)

    async def get(self, user_id: int):
        return await self.adapter.get(user_id)
