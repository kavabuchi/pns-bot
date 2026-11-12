"""HTTP-клиент для ПНС: авторизация и получение HTML нужных страниц.

Подсказки:
  - aiohttp уже стоит вместе с aiogram, можно использовать aiohttp.ClientSession
  - сессия хранит cookie после логина — переиспользуй её, а не логинься на каждый запрос
  - если сайт рисует данные через JavaScript (в HTML-ответе пусто) —
    поищи в DevTools -> Network JSON-запрос (XHR/fetch), часто проще брать данные оттуда
"""


class PnsAuthError(Exception):
    """Не удалось войти (неверный пароль, протухла сессия и т.п.)."""


class PnsClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        # TODO: создать/хранить сессию

    async def login(self, username: str, password: str) -> None:
        """Войти в ПНС. При неудаче — raise PnsAuthError."""
        # TODO
        raise NotImplementedError

    async def fetch_deadlines_page(self) -> str:
        """Вернуть HTML (или JSON-текст) страницы, где перечислены задания."""
        # TODO
        raise NotImplementedError

    async def close(self) -> None:
        """Закрыть сессию."""
        # TODO
        raise NotImplementedError
