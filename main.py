from fastapi import FastAPI, APIRouter


app = FastAPI()
UserRouter = APIRouter()

@UserRouter.get('/')
def HelloWorld():
    return 'Hello world'

app.include_router(prefix='/users', router=UserRouter)