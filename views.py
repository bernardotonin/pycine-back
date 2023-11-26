from fastapi import APIRouter, HTTPException
from services import UserService, FavoriteService, FavoriteActorService
from schemas import UserCreateInput, UserFavoriteAddInput, StandardOutput, ErrorOutput, UserOutput, SearchActorByIdOutput, ListMoviesOutput, SearchActorByNameOutput, UserFavoriteActorAddInput
from typing import List
import requests
from tmdb import get_json, get_actor


user_router = APIRouter(prefix='/user')
movie_router = APIRouter(prefix='/movie')

# ===========================================
#              Movie Features

# FAVORITA ARTISTA

@movie_router.post("/actor/favorite", response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def list_actor(favActor_input: UserFavoriteActorAddInput):
    try:
        FavoriteActorService.add_favorite_actor(user_id=favActor_input.user_id, name=favActor_input.name, bio=favActor_input.bio, profileUrl=favActor_input.profileUrl, tmdb_actor_id=favActor_input.tmdb_actor_id)
        return StandardOutput(message='Ok')
    except Exception as error:
        raise HTTPException(400, detail=str(error))
# LISTA ARTISTA POR NOME

@movie_router.get("/actor", response_model=List[SearchActorByNameOutput], responses={400: {'model': ErrorOutput}})
async def list_actor(query: str):
    try:
        data = get_json(
            "/search/person", f"?query={query}"
        )
        result = data['results']
        filtro = []
        for actor in result:
            filtro.append({
                "name": actor['name'],
                "profile_picture": f"https://image.tmdb.org/t/p/w185{actor['profile_path']}",
                "known_for": actor['known_for_department'],
                "tmdb_actor_id": actor['id']
            })
        return filtro
    except Exception as error:
        raise HTTPException(400, detail=str(error))


# LISTA FILME POR NOME
@movie_router.get("/search", response_model=List[ListMoviesOutput], responses={400: {'model': ErrorOutput}})
async def list_movies_by_name(query: str):
    try:
        data = get_json(
            "/search/movie", f"?query={query}"
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
    except Exception as error:
        raise HTTPException(400, detail=str(error))


# LISTA TODOS OS FILMES
@movie_router.get("/list", response_model=List[ListMoviesOutput], responses={400: {'model': ErrorOutput}})
async def list_movies():
    try:
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
                "tmdb_id": movie['id']
            })
        return filtro
    except Exception as error:
        raise HTTPException(400, detail=str(error))

# LISTA ATOR POR ID

@movie_router.get("/actor/{actor_id}", response_model=SearchActorByIdOutput, responses={400: {'model': ErrorOutput}})
async def list_actor(actor_id: int):
    try:
        data = get_actor(actor_id)
        result = {
            "name": data['name'],
            "bio": data['biography'],
            "known_for": data['known_for_department'],
            "birthday": data['birthday'],
            "placeofbirth": data['place_of_birth']
        }
        return result
    except Exception as error:
        raise HTTPException(400, detail=str(error))
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
        FavoriteService.add_favorite(user_id=favorite_add.user_id, title=favorite_add.title, description=favorite_add.description, bannerUrl=favorite_add.bannerUrl, tmdb_id=favorite_add.tmdb_id)
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

@user_router.get('/list', response_model=List[UserOutput], responses={400: {'model': ErrorOutput}})
def user_list():
    try:
        return UserService.list_users()
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
## LISTA USUARIO POR ID
    
@user_router.get('/list/{user_id}', response_model=UserOutput, responses={400: {'model': ErrorOutput}})
def user_list_by_id(user_id : int):
    try:
        return UserService.list_user_by_id(user_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))
