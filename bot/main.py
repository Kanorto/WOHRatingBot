from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

# TODO: move to config
API_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start", "help"])
async def send_welcome(message: types.Message):
    await message.reply("Welcome to WOH Rating Bot!")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
