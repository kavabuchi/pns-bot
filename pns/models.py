"""Структуры данных, с которыми работает весь бот."""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Deadline:
    # TODO: сверь с полями в .ics и поправь, если нужно
    id: str            # UID события — уникальный, чтобы не слать дубли
    subject: str       # CATEGORIES — предмет
    title: str         # SUMMARY — название
    due_at: datetime   # DTSTART — срок (уже в киевском времени)
