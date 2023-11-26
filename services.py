from database.models import User, Favorite, FavoriteActor
from database.connection import SessionLocal
from sqlalchemy import delete, select
from fastapi import HTTPException


class UserService: 
    def create_user(email: str, password: str):
        with SessionLocal() as session:
            session.add(User(email = email, password=password))
            session.commit()

    def delete_user(user_id: int):
        with SessionLocal() as session:
            session.execute(delete(User).where(User.id==user_id))
            session.execute(delete(Favorite).where(Favorite.user_id == user_id))
            session.execute(delete(FavoriteActor).where(FavoriteActor.user_id == user_id))
            session.commit()

    def list_users():
        with SessionLocal() as session:
            result = session.execute(select(User))
            return result.scalars().all()
        
    def list_user_by_id(user_id: int):
        with SessionLocal() as session:
            result = session.execute(select(User).where(User.id==user_id))
            return result.scalars().first()
        
class FavoriteService:
    def get_favorites_by_title(title: str):
        with SessionLocal() as session:
            return session.query(Favorite).filter(Favorite.title.ilike(f'%{title}%')).all()
    def add_favorite(user_id: int, title: str, description: str, bannerUrl: str, tmdb_id: int):
        with SessionLocal() as session:
            if(FavoriteService.get_favorites_by_title(title=title)):
                raise HTTPException(400)
            session.add(Favorite(title=title, description=description, bannerUrl=bannerUrl, user_id=user_id, tmdb_id=tmdb_id))
            session.commit()
    def remove_favorite(user_id: int, title: str):
        with SessionLocal() as session:
            session.execute(delete(Favorite).where(Favorite.user_id==user_id, Favorite.title==title))
            session.commit()

class FavoriteActorService:
    def add_favorite_actor(user_id: int, name: str, bio: str, profileUrl: str, tmdb_actor_id: int):
        with SessionLocal() as session:
            session.add(FavoriteActor(name=name, bio=bio, profileUrl=profileUrl, tmdb_actor_id=tmdb_actor_id, user_id=user_id))
            session.commit()

    def remove_favorite(user_id: int, name: str):
        with SessionLocal() as session:
            session.execute(delete(FavoriteActor).where(FavoriteActor.user_id==user_id, FavoriteActor.name==name))
            session.commit()