from connection import engine
from models import Base

def create_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    create_database()