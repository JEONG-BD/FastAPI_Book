from pydantic import BaseModel, EmailStr
from typing import Optional, List
from beanie import Document, Link 
from models.events import Event 


class User(Document):
    email : EmailStr
    password : str 
    # events : Optional[List[Event]] = None 
    
    class Settings :
       name = 'users'
    
    
    class Config :
        schema_extra = {
            'example':{
                'email':'fastapi@test.com',
                'username': 'strong',
            }
        }


class UserSignIn(BaseModel):
    email:EmailStr
    password : str 


class TokenResponse(BaseModel):
    access_token: str 
    token_type: str 