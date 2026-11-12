"""Структуры данных, с которыми работает весь бот."""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Deadline:
    # TODO: посмотри, какие поля реально есть на сайте, и поправь список
    id: str            # уникальный id работы (из ссылки/атрибута) — чтобы не слать дубли
    subject: str       # предмет
    title: str         # название работы
    due_at: datetime   # срок сдачи
    url: str | None = None
    submitted: bool = False
