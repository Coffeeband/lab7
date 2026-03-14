import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# У реальному проекті токен береться з .env
API_TOKEN = 'YOUR_BOT_TOKEN_HERE'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Вітаю у SmartHunt! Я допоможу тобі знайти фріланс-проєкти.")

async def main():
    print("Бот SmartHunt запущений...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())