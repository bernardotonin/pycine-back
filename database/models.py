from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    password = Column(String)
    favorites = relationship('Favorite', backref='user')
    

class Favorite(Base):
    __tablename__= 'favorite'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    description = Column(String)
    bannerUrl = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))