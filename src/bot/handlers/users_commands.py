from aiogram import Router, types, F
from aiogram.filters import CommandStart
from bot.messages_texts import COMMAND_START
from services.content_delivery import find_news

router = Router()

@router.message(CommandStart())
async def start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username

    await message.answer(
        COMMAND_START.format(username=username), 
        #reply_markup=keyboard
    )

# This is a test handler
@router.message(F.text == 'Search news')
async def search_news(message: types.Message):
    news = await find_news()