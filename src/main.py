import os
import asyncio
import logging
from bot.handlers import users_commands
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

async def main():
    dp.include_router(router=users_commands.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())