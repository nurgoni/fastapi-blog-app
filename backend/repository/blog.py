from sqlalchemy.orm import Session
from schemas.blog import CreateBlog, ShowBlog, UpdateBlog
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

def retrieve_blog(id: int, db: Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    response = ShowBlog(
        title=blog.title,
        content=blog.content,
        created_at=blog.created_at.date(),
    )
    return response

def list_blogs(db: Session):
    blogs = db.query(Blog).filter(Blog.is_active == True).all()
    return blogs

def update_blog(id: int, blog: UpdateBlog, author_id: int, db: Session):
    blog_in_db = db.query(Blog).filter(Blog.id == id).first()

    if not blog_in_db:
        return {"error": f"Blog with id {id} does not exist"}
    if not blog_in_db.author_id == author_id:
        return {"error": f"Only the author can modify the blog"}

    blog_in_db.title = blog.title
    blog_in_db.content = blog.content

    db.add(blog_in_db)
    db.commit()

    return blog_in_db

def delete_blog(id: int, author_id: int, db: Session):
    blog_in_db = db.query(Blog).filter(Blog.id == id).first()

    if not blog_in_db:
        return {"error": f"Blog with id {id} does not exist"}
    if not blog_in_db.author_id == author_id:
        return {"error": f"Only the author can delete a blog"}

    blog_in_db.delete()
    db.commit()

    return {"message": f"Successfully deleted blog with id {id}"}
