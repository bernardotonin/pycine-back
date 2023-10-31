from fastapi import APIRouter, HTTPException
from services import UserService, FavoriteService
from schemas import UserCreateInput, UserFavoriteAddInput, StandardOutput, ErrorOutput, UserListOutput
from typing import List

from tmdb import get_json, get_actor


user_router = APIRouter(prefix='/user')
movie_router = APIRouter(prefix='/movie')

# ===========================================
#              Movie Features
#
@movie_router.get("/list")
async def list_movies():
    data = get_json(
        "/discover/movie", "?sort_by=vote_count.desc"
    )
    results = data['results']
    filtro = []
    for movie in results:
        filtro.append({
            "title": movie['original_title'], 
            "image": f"https://image.tmdb.org/t/p/w185{movie['poster_path']}",
            "description": movie['overview'],
        })
    return filtro

@movie_router.get("/actor/{actor_id}")
async def list_actor(actor_id: int):
    data = get_actor(actor_id)
    result = {
        "name": data['name'],
        "bio": data['biography'],
        "known_for": data['known_for_department'],
        "birthday": data['birthday'],
        "placeofbirth": data['place_of_birth']
    }
    return result
# ===========================================
#              User Features
#

## CRIAR USER

@user_router.post('/create', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
def user_create(user_input : UserCreateInput):
    try:
        UserService.create_user(email=user_input.email, password=user_input.password)
        return StandardOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
## DELETAR USER
    
@user_router.delete('/delete/{user_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
def user_delete(user_id: int):
    try:
        UserService.delete_user(user_id)
        return StandardOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
## ADD FAVORITO
    
@user_router.post('/favorite/add', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
def user_favorite_add(favorite_add: UserFavoriteAddInput):
    try:
        FavoriteService.add_favorite(user_id=favorite_add.user_id, title=favorite_add.title, description=favorite_add.description, bannerUrl=favorite_add.bannerUrl)
        return StandardOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
## DELETA FAVORITO
    
@user_router.delete('/favorite/remove/{user_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
def user_favorite_remove(user_id: int, title: str):
    try:
        FavoriteService.remove_favorite(user_id=user_id, title=title)
        return StandardOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
## LISTA USUARIOS

@user_router.get('/list', response_model=List[UserListOutput], responses={400: {'model': ErrorOutput}})
def user_list():
    try:
        return UserService.list_users()
    except Exception as error:
        raise HTTPException(400, detail=str(error))
