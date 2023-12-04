import requests
import json

api_key = '427e093ceed957451c6a62d5358506e8'

def get_json(endpoint, params=None):
    """ 
    fornecido o endpoint faz o request e retorna o resultado em json
    """
    url = f"https://api.themoviedb.org/3{endpoint}{params}&api_key={api_key}"
    response = requests.get(url)
    return response.json()


def get_actor(user_id : int):
    url = f"https://api.themoviedb.org/3/person/{user_id}?api_key={api_key}"
    response = requests.get(url)
    return response.json()

def movieFilter(results):
    filtro = []
    for movie in results:
        filtro.append({
            "title": movie['original_title'], 
            "image": f"https://image.tmdb.org/t/p/w185{movie['poster_path']}",
            "description": movie['overview'],
            "tmdb_id": movie['id']
        })
    return filtro

def actorByIdFilter(data):
    result = {
            "name": data['name'],
            "bio": data['biography'],
            "known_for": data['known_for_department'],
            "birthday": data['birthday'],
            "placeofbirth": data['place_of_birth']
    }
    return result

def actorByNameFilter(results):
    filtro = []
    for actor in results:
        filtro.append({
            "name": actor['name'],
            "profile_picture": f"https://image.tmdb.org/t/p/w185{actor['profile_path']}",
            "known_for": actor['known_for_department'],
            "tmdb_actor_id": actor['id']
        })
    return filtro

