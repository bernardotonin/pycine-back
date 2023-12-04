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
    tmdb_id: int

class UserFavoriteActorAddInput(BaseModel):
    name: str
    bio: str
    profileUrl: str
    user_id: int
    tmdb_actor_id: int
    
class Favorite(BaseModel):
    id: int
    title: str
    description: str
    bannerUrl: str
    user_id: int
    tmdb_id: int

    class Config:
        orm_mode = True

class FavoriteActor(BaseModel):
    id: int
    name: str
    bio: str
    profileUrl: str
    user_id: int
    tmdb_actor_id: int

    class Config:
        orm_mode = True

class UserOutput(BaseModel):
    id: int
    email: str
    password: str
    favorites: List[Favorite]
    favorite_actors: List[FavoriteActor]
    
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
    tmdb_actor_id: int
    popularity: float

class ListMoviesOutput(BaseModel):
    title: str
    image: str
    description: str
    tmdb_id: int