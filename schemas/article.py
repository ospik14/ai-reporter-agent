from pydantic import BaseModel

class ArticleBase(BaseModel):
    title: str
    description: str
    link: str
    publication_date: str