from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from port.factory.user import user_factory

from ..entities.dto.token.tokenDataDto import TokenData
from ..entities.dto.user.userDto import User
from domain.service.user import UserService
from passlib.exc import UnknownHashError
from domain.entities.dto.user.registerDto import RegisterUserDTO
from domain.entities.dto.user.userDto import User

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def authenticate_user(username: str, password: str, service: UserService = user_factory()):
    user = await service.getPerEmail(email=username)
    if not user:
        return False
    try:
        if not verify_password(password, user.password):
            return False
    except UnknownHashError as E:
        credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid JWT format",
        headers={"WWW-Authenticate": "Bearer"},
        )
        raise credentials_exception

    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def create_user(new_user: RegisterUserDTO, service: UserService = user_factory()):
    new_user.password = get_password_hash(new_user.password)
    user  = await service.create(new_user);

    return User(email=user.email, first_name=user.first_name, last_name=user.last_name, active=user.active, username=user.email)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], service: UserService = user_factory()):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await service.getPerEmail(email=username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if not current_user.active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return User(email=current_user.email, first_name=current_user.first_name, last_name=current_user.last_name, active=current_user.active, username=current_user.email)
