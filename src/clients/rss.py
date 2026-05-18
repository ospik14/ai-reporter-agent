import uuid
from httpx import AsyncClient
from schemas.article import ArticleBase
from feedparser import parse

async def fetch_rss(url: str):
    async with AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise
        
        feed = parse(response.text) 
        articles = []
        for entry in feed.entries:
            articles.append(
                ArticleBase(
                    id=str(uuid.uuid4()),
                    title=entry.title,
                    description=entry.description,
                    link=entry.link,
                    publication_date=entry.published
                )
            )

        return articles