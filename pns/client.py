"""Скачивание календаря ПНС (.ics) по ссылке экспорта Moodle.

Логин не нужен: в ссылке уже есть authtoken.

Подсказки:
  - aiohttp уже стоит вместе с aiogram: aiohttp.ClientSession
  - поставь таймаут: aiohttp.ClientTimeout(total=...)
  - при неверном токене Moodle вернёт не календарь, а страницу с ошибкой —
    проверь статус и/или что текст начинается с BEGIN:VCALENDAR
"""


class PnsLinkError(Exception):
    """Ссылка не работает: неверный/устаревший токен, сайт вернул не календарь."""


async def fetch_calendar(url: str) -> str:
    """Скачать .ics по ссылке и вернуть его текст. При проблеме — raise PnsLinkError."""
    # TODO
    raise NotImplementedError
