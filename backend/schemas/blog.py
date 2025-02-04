from typing import Optional
from pydantic import BaseModel, root_validator
from datetime import date


class CreateBlog(BaseModel):
    title: str
    slug: str
    content: str

    @root_validator(pre=True)
    def generate_slug(cls, values):
        if "title" in values:
            values["slug"] = values.get("title").replace(" ", "-").lower()
        return values
    

class ShowBlog(BaseModel):
    title: str
    content: Optional[str]
    created_at: date

    class Config():
        from_attributes = True

