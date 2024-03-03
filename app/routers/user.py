from fastapi import APIRouter, status, Depends
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import user

get_db = database.get_db

router = APIRouter(
    prefix="/user",
    tags=["users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session=Depends(get_db)):
    return user.create_user(request, db)

@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id, db:Session=Depends(get_db)):
    return user.get_user(id, db)