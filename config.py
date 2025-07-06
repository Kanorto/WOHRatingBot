import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///woh_rating.db")
DEBUG = os.getenv("DEBUG", "False").lower() in ("1", "true", "yes")
