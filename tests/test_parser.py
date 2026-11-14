"""Тесты парсера. Запуск: python -m pytest

TODO: скачай свой календарь по ссылке и сохрани как tests/fixtures/calendar.ics
      (файл в .gitignore — там личные данные).
"""
from pathlib import Path

FIXTURES = Path(__file__).parent / "fixtures"


def test_is_deadline():
    # assert is_deadline("Філософська антропологія завершується") is True
    # assert is_deadline("Відвідуваність (Група ...)") is False
    pass


def test_parse_deadlines():
    # text = (FIXTURES / "calendar.ics").read_text(encoding="utf-8")
    # deadlines = parse_deadlines(text)
    # assert len(deadlines) == ...
    pass
