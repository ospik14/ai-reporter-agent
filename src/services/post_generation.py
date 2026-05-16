from clients.rss import fetch_rss

async def generate_post():
    articles = await fetch_rss('https://www.bleepingcomputer.com/feed/')
    