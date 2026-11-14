"""Все настройки из .env в одном месте. Остальной код импортирует их отсюда."""
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

# Твоя ссылка экспорта календаря ПНС. Нужна до этапа 8 — потом ссылки будут храниться в Redis.
PNS_CALENDAR_URL = os.getenv("PNS_CALENDAR_URL")

# Как часто проверять дедлайны (в минутах)
CHECK_INTERVAL_MINUTES = int(os.getenv("CHECK_INTERVAL_MINUTES", "60"))

# За сколько часов до дедлайна напоминать, например "72,24,3"
REMIND_BEFORE_HOURS = [int(h) for h in os.getenv("REMIND_BEFORE_HOURS", "72,24,3").split(",")]

# TODO: подумай, что делать, если BOT_TOKEN не задан (упасть сразу с понятной ошибкой?)
