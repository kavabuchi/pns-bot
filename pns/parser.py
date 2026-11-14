"""Превращает текст .ics в список Deadline.

Чистые функции без сети — их легко тестировать на сохранённом файле (tests/fixtures/calendar.ics).
Подсказка: from icalendar import Calendar; Calendar.from_ical(text).walk("VEVENT")
"""
from pns.models import Deadline


def is_deadline(summary: str) -> bool:
    """Решить по названию события, дедлайн это или нет.

    В календаре много лишнего: «Відвідуваність…», «Лекція…».
    TODO: по признакам, которые ты выписал в README («Заметки»), вернуть True/False.
    """
    raise NotImplementedError


def parse_deadlines(ics_text: str) -> list[Deadline]:
    # TODO: пройти по событиям, оставить только дедлайны (is_deadline)
    # TODO: DTSTART в UTC -> перевести в Europe/Kyiv (zoneinfo)
    raise NotImplementedError
