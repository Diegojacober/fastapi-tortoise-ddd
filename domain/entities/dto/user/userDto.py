from pydantic import BaseModel, EmailStr
from typing import Optional

class UserDTO(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    password: str
    email: EmailStr
