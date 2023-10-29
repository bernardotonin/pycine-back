from database.models import User
from database.connection import SessionLocal


class UserService: 
    def create_user(name):
        with SessionLocal() as session:
            session.add(User(name = name))
            session.commit()
            