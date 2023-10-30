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


