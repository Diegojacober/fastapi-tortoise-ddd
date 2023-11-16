from pydantic import BaseModel
from adapter.user import UserTortoiseAdapter
from domain.entities.dto.user.registerDto import RegisterUserDTO

class UserService(BaseModel):

    adapter: UserTortoiseAdapter

    async def listAll(self):
        return await self.adapter.listAll()

    async def create(self, user: RegisterUserDTO):
        return await self.adapter.create(user)

    async def get(self, user_id: int):
        return await self.adapter.get(user_id)
    
    async def getPerEmail(self, email: str):
        return await self.adapter.getPerEmail(email=email)
