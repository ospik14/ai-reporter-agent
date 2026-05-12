import asyncio
from httpx import AsyncClient

async def get_feed(url: str):
    async with AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise

        return response.text


asyncio.run(get_feed('https://www.bleepingcomputer.com/feed/'))