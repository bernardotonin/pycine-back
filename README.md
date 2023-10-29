Utilizado o pacote pipenv para realizar o backend

pip install --user pipenv
python3 -m pipenv shell
pipenv install
python3 -m

bodys:

create user:
{
    "email": str
    "password": str
}

favorite add:
{
    "user_id": int
    "title": str
    "description": str
    "bannerUrl": str
}

http://localhost:8080/user/favorite/remove/1?title=Fight+Club