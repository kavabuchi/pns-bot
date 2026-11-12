"""Обёртка над Redis, чтобы остальной код не знал про ключи и команды Redis.

Что нужно хранить (идея ключей):
  user:{chat_id}                    -> данные для входа в ПНС
  users                             -> set всех chat_id (чтобы планировщик знал, кого проверять)
  notified:{chat_id}:{deadline_id}  -> отметка «уже напоминали за N часов»

TODO: используй redis.asyncio (асинхронный клиент), раз бот на asyncio.
TODO: подумай о TTL для notified:* — после дедлайна они больше не нужны.
TODO: пароль в открытом виде в Redis — плохо. Почитай про шифрование (cryptography.fernet).
"""


class Repository:
    def __init__(self, redis_url: str) -> None:
        # TODO
        raise NotImplementedError

    async def save_user(self, chat_id: int, username: str, password: str) -> None:
        raise NotImplementedError

    async def get_user(self, chat_id: int) -> dict | None:
        raise NotImplementedError

    async def delete_user(self, chat_id: int) -> None:
        raise NotImplementedError

    async def all_chat_ids(self) -> list[int]:
        raise NotImplementedError

    async def was_notified(self, chat_id: int, deadline_id: str, hours_before: int) -> bool:
        raise NotImplementedError

    async def mark_notified(self, chat_id: int, deadline_id: str, hours_before: int) -> None:
        raise NotImplementedError
