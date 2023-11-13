from typing import TypeVar
from pydantic import BaseModel

DataT = TypeVar("DataT")

class UserTortoiseAdapter(BaseModel):

    model: DataT
    
    async def listAll(self):
        return await self.model.all()

    async def create(self, post: Post):
        return await self.model.create(**post.dict())

    async def get(self, user_id: int):
        return await self.model.get(id=user_id)
