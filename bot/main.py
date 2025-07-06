from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

from config import BOT_TOKEN, DEBUG

logging.basicConfig(level=logging.DEBUG if DEBUG else logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("Welcome to WOH Rating Bot!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
