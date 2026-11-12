"""Точка входа: собирает бота, подключает хендлеры, запускает планировщик и polling."""
import asyncio
import logging

import config  # noqa: F401  (config.BOT_TOKEN, config.REDIS_URL и т.д.)


async def main() -> None:
    logging.basicConfig(level=logging.INFO)

    # TODO 1: создать Bot(token=...) и Dispatcher() из aiogram
    # TODO 2: подключить роутеры из bot/handlers (dp.include_router(...))
    # TODO 3: создать подключение к хранилищу (storage/repository.py)
    # TODO 4: запустить планировщик проверки дедлайнов (scheduler/jobs.py)
    # TODO 5: await dp.start_polling(bot)
    raise NotImplementedError


if __name__ == "__main__":
    asyncio.run(main())
