from fastapi import APIRouter, HTTPException
from services import UserService, FavoriteService
from schemas import UserCreateInput, UserFavoriteAddInput, StandardOutput, ErrorOutput, UserListOutput
from typing import List


user_router = APIRouter(prefix='/user')
movie_router = APIRouter(prefix='/movie')

@user_router.post('/create', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
def user_create(user_input : UserCreateInput):
    try:
        UserService.create_user(email=user_input.email, password=user_input.password)
        return StandardOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
@user_router.delete('/delete/{user_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
def user_delete(user_id: int):
    try:
        UserService.delete_user(user_id)
        return StandardOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
@user_router.post('/favorite/add', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
def user_favorite_add(favorite_add: UserFavoriteAddInput):
    try:
        FavoriteService.add_favorite(user_id=favorite_add.user_id, title=favorite_add.title, description=favorite_add.description, bannerUrl=favorite_add.bannerUrl)
        return StandardOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
@user_router.delete('/favorite/remove/{user_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
def user_favorite_remove(user_id: int, title: str):
    try:
        FavoriteService.remove_favorite(user_id=user_id, title=title)
        return StandardOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@user_router.get('/list', response_model=List[UserListOutput], responses={400: {'model': ErrorOutput}})
def user_list():
    try:
        return UserService.list_users()
    except Exception as error:
        raise HTTPException(400, detail=str(error))