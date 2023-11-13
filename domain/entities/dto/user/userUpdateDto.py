from pydantic import BaseModel, EmailStr
from typing import Optional

class UserUpdateDTO(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    password: Optional[str]
    email: Optional[EmailStr]
