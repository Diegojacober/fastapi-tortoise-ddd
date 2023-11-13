from pydantic import BaseModel, EmailStr

class RegisterUserDTO(BaseModel):
    first_name: str
    last_name: str
    password: str
    email = EmailStr
