from clients.rss import fetch_rss
from clients.ai_request import content_selection

async def generate_post():
    articles = await fetch_rss('https://www.bleepingcomputer.com/feed/')
    await content_selection(articles)
    