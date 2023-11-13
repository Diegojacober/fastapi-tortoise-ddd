from typing import TypeVar
from pydantic import BaseModel
from domain.entities.dto.user.registerDto import RegisterUserDTO

DataT = TypeVar("DataT")

class UserTortoiseAdapter(BaseModel):

    model: DataT
    
    async def listAll(self):
        return await self.model.all()

    async def create(self, user: RegisterUserDTO):
        return await self.model.create(**user.dict())

    async def get(self, user_id: int):
        return await self.model.get(id=user_id)
