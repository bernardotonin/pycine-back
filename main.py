from fastapi import FastAPI, APIRouter


app = FastAPI()
router = APIRouter()

@router.get('/')
def HelloWorld():
    return 'Hello world'

app.include_router(prefix='/users', router=router)