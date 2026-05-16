from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from bot.messages_texts import COMMAND_START
from services.post_generation import generate_post

router = Router()

@router.message(CommandStart())
async def start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username

    await message.answer(
        COMMAND_START.format(username=username), 
        #reply_markup=keyboard
    )

@router.message(Command('new_post'))
async def create_post(message: types.Message):
    post_data = await generate_post()