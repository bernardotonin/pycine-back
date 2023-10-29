from fastapi import FastAPI, APIRouter

from views import user_router, movie_router

app = FastAPI()
router = APIRouter()

@router.get('/')
def HelloWorld():
    return 'Hello world'

app.include_router(prefix='/first', router=router)
app.include_router(user_router)
app.include_router(movie_router)