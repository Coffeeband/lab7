import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command


API_TOKEN = 'YOUR_BOT_TOKEN_HERE'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Вітаю у SmartHunt! Я допоможу тобі знайти фріланс-проєкти.")

