from sqlalchemy.orm import Session
from schemas.blog import CreateBlog, ShowBlog
from db.models import Blog


def create_new_blog(blog: CreateBlog, db: Session, author_id: int=1):
    blog = Blog(**blog.dict(), author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)

    response = ShowBlog(
        title=blog.title,
        content=blog.content,
        created_at=blog.created_at.date(),
    )

    return response
