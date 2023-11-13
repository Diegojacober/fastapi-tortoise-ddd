from fastapi import APIRouter, Depends
from domain.entities.dto.user.loginDto import LoginDTO
from domain.entities.dto.user.registerDto import RegisterUserDTO
from domain.entities.dto.user.userDto import UserDTO
from domain.entities.dto.user.userUpdateDto import UserUpdateDTO
from domain.service.user import UserService

from port.factory.user import user_factory

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},

)


@router.get("/",)
async def list_users(service: UserService = Depends(user_factory)):
    return await service.listAll()

@router.post("/",)
async def create_user(body: RegisterUserDTO, service: UserService = Depends(user_factory)):
    user = RegisterUserDTO(**body.dict())
    return await service.create(user)

@router.get("/{post_id}",)
async def get_post(user_id: int, service: UserService = Depends(user_factory)):
    return await service.get(user_id)
