from fastapi import APIRouter, Depends
from domain.entities.dto.user.userDbDto import UserInDB
from fastapi import Depends, HTTPException, status
from domain.entities.dto.token.tokenDto import Token
from domain.entities.dto.user.loginDto import LoginDTO
from domain.entities.dto.user.registerDto import RegisterUserDTO
from domain.entities.dto.user.userDto import User
from datetime import timedelta
from typing import Annotated
from domain.service.auth import *;

from port.factory.user import user_factory

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    responses={404: {"description": "Not found"}},

)


@router.post("/token", response_model=Token)
async def login_for_access_token(
    req: LoginDTO
):
    user = await authenticate_user( req.email, req.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=User)
async def register_user(req: RegisterUserDTO):
    return await create_user(req)

@router.get("/me/", response_model=User)
async def read_users_me(user: User = Depends(get_current_active_user)):
    return user


@router.get("/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]