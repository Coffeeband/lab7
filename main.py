import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command



API_TOKEN = 'YOUR_BOT_TOKEN_HERE'


bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привіт фрілансер, готовий робити роботу?")

async def main():
    print("Бот працює...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

