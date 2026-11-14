"""/deadlines — показать ближайшие дедлайны прямо сейчас (по запросу)."""
from aiogram import Router

router = Router()

# TODO: взять ссылку пользователя (сначала из config.PNS_CALENDAR_URL, потом из storage)
# TODO: pns.client.fetch_calendar -> pns.parser.parse_deadlines
# TODO: только будущие, по дате, отформатировать (см. bot/texts.py)
