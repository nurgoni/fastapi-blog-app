from fastapi import APIRouter, status, HTTPException
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

from db.session import get_db
from db.models import User
from schemas.blog import ShowBlog, CreateBlog, UpdateBlog
from repository.blog import create_new_blog, retrieve_blog, list_blogs

from api.v1.route_login import get_current_user

router = APIRouter()

@router.post("/blog", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
async def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db, author_id=1)
    return blog

@router.get("/blog/{id}", response_model=ShowBlog)
async def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retrieve_blog(id=id, db=db)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Blog with id {id} does not exist"
        )
    return blog

@router.get("/blog/", response_model=List[ShowBlog])
async def get_all_blogs(db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return blogs

@router.put("/blog/{id}", response_model=ShowBlog)
def update_blog(id: int, blog: UpdateBlog, db: Session = Depends(get_db), current_user: User=Depends(get_current_user)):
    blog = update_blog(id=id, blog=blog, author_id=current_user.id, db=db)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Blog with id {id} does not exist"
        )
    return blog

@router.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db), current_user: User=Depends(get_current_user)):
    message = delete_blog(id=id, author_id=current_user.id, db=db)
    if message.get("error"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=message.get("error")
        )
    return {"message": f"Successfully deleted blog with id {id}"}
