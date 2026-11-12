"""Тесты парсера. Запуск: python -m pytest

TODO: сохрани страницу ПНС с заданиями (Ctrl+S в браузере) в tests/fixtures/deadlines.html
      (убери оттуда личные данные!) и проверь, что parse_deadlines вытаскивает нужное.
"""
from pathlib import Path

FIXTURES = Path(__file__).parent / "fixtures"


def test_parse_deadlines():
    # html = (FIXTURES / "deadlines.html").read_text(encoding="utf-8")
    # deadlines = parse_deadlines(html)
    # assert len(deadlines) == ...
    pass
