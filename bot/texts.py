"""Тексты и форматирование сообщений, чтобы не держать строки внутри хендлеров."""
from pns.models import Deadline


def format_deadline(deadline: Deadline) -> str:
    """Одна строка про один дедлайн: предмет, название, дата, сколько осталось."""
    # TODO
    raise NotImplementedError


def format_deadline_list(deadlines: list[Deadline]) -> str:
    """Список дедлайнов одним сообщением. Не забудь случай, когда список пуст."""
    # TODO
    raise NotImplementedError
