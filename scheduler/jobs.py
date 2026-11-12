"""Раз в CHECK_INTERVAL_MINUTES обходит всех пользователей и шлёт напоминания.

Варианты запуска:
  - простой: asyncio-цикл  while True: await check(); await asyncio.sleep(...)
  - удобный: APScheduler (AsyncIOScheduler) — scheduler.add_job(check, "interval", minutes=...)
"""


async def check_all_users(bot, repo) -> None:
    """Одна проверка.

    Для каждого chat_id:
      1. взять данные входа из repo
      2. залогиниться (pns.client), получить страницу, распарсить (pns.parser)
      3. для каждого несданного дедлайна и каждого порога из REMIND_BEFORE_HOURS:
           если до дедлайна осталось <= порога и ещё не напоминали — отправить и mark_notified
    TODO: ошибка у одного пользователя не должна ронять проверку остальных (try/except + logging)
    """
    raise NotImplementedError


def start_scheduler(bot, repo) -> None:
    """Запустить периодический вызов check_all_users."""
    raise NotImplementedError
