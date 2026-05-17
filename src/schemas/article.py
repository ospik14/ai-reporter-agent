from pydantic import BaseModel

class ArticleBase(BaseModel):
    id: str
    title: str
    description: str
    link: str
    publication_date: str