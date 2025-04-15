from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name : str
    email : EmailStr

class GroupCreate(BaseModel):
    name : str