"""Превращает HTML страницы ПНС в список Deadline.

Чистая функция без сети — её легко тестировать на сохранённом HTML (tests/fixtures).
Подсказка: BeautifulSoup (beautifulsoup4) — soup.select("css-селектор").
"""
from pns.models import Deadline


def parse_deadlines(html: str) -> list[Deadline]:
    # TODO: найти в DevTools, в каких тегах/классах лежат работы и даты
    # TODO: дату из строки -> datetime (datetime.strptime, учти формат и часовой пояс)
    raise NotImplementedError
