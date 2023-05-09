'''This module defines the HTTP request/response schemas for the /symbol FastAPI routers.'''

from enum import Enum
from datetime import date
from pydantic import BaseModel, EmailStr


# Enumerations
class Example(str, Enum):
    '''Example values.'''

    CAD = 'CAD'
    USD = 'USD'


# Requests
class CreateUserRequest(BaseModel):
    '''Request schema to /user/create'''

    email: EmailStr
    password: str


class UpdateUserRequest(BaseModel):
    '''Request schema to /user/update'''

    email: EmailStr
    password: str
    isActive: bool
    example: Example


# Responses
class UserResponse(BaseModel):
    '''Response schema to /user/*'''

    email: str
    isActive: bool
    createdAt: date
    updatedAt: date
