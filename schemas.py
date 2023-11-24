from pydantic import BaseModel
from typing import List

class UserCreateInput(BaseModel):
    email: str
    password: str

class UserFavoriteAddInput(BaseModel):
    user_id: int
    title: str
    description: str
    bannerUrl: str
    
class Favorite(BaseModel):
    id: int
    title: str
    description: str
    bannerUrl: str
    user_id: int

    class Config:
        orm_mode = True

class UserOutput(BaseModel):
    id: int
    email: str
    password: str
    favorites: List[Favorite]
    
    class Config:
        orm_mode = True

class StandardOutput(BaseModel):
    message: str

class ErrorOutput(BaseModel):
    details: str

class SearchActorByIdOutput(BaseModel):
    name: str
    bio: str
    known_for: str
    birthday: str
    placeofbirth: str

class SearchActorByNameOutput(BaseModel):
    name: str
    profile_picture: str
    known_for: str

class ListMoviesOutput(BaseModel):
    title: str
    image: str
    description: str