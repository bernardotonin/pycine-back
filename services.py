from database.models import User, Favorite
from database.connection import SessionLocal
from sqlalchemy import delete, select


class UserService: 
    def create_user(email: str, password: str):
        with SessionLocal() as session:
            session.add(User(email = email, password=password))
            session.commit()

    def delete_user(user_id: int):
        with SessionLocal() as session:
            session.execute(delete(User).where(User.id==user_id))
            session.execute(delete(Favorite).where(Favorite.user_id == user_id))
            session.commit()

    def list_users():
        with SessionLocal() as session:
            result = session.execute(select(User))
            return result.scalars().all()
        
    def list_user_by_id(user_id: int):
        with SessionLocal() as session:
            result = session.execute(select(User).where(User.id==user_id))
            return result.scalars().first();
        
class FavoriteService:
    def add_favorite(user_id: int, title: str, description: str, bannerUrl: str):
        with SessionLocal() as session:
            session.add(Favorite(title=title, description=description, bannerUrl=bannerUrl, user_id=user_id))
            session.commit()
    def remove_favorite(user_id: int, title: str):
        with SessionLocal() as session:
            session.execute(delete(Favorite).where(Favorite.user_id==user_id, Favorite.title==title))
            session.commit()