from dataclasses import dataclass, field
from string import Template

from aiogram import types, Bot
from aiogram.utils import markdown as m


@dataclass
class SendingData:
    uid: str
    text: str | Template
    url: str
    btn_title: str
    photo: str | None = None
    video: str | None = None

    kb: types.InlineKeyboardMarkup = field(init=False)
    count: int = field(init=False)

    async def get_text(self, bot: Bot, user_id: int, name: str = None):
        if isinstance(self.text, str):
            return self.text
        else:
            if name is None:
                chat_member = await bot.get_chat_member(user_id, user_id)
                name = chat_member.user.first_name
            name = m.quote_html(name)
            return self.text.substitute(name=name)

    def __post_init__(self):
        self.kb = types.InlineKeyboardMarkup()
        self.kb.add(types.InlineKeyboardButton(self.btn_title, url=self.url))
        # self.kb.add(types.InlineKeyboardButton('🎁 Получить подарок', url=self.url))
        # self.kb.add(types.InlineKeyboardButton('🎁 Получить подарок', callback_data="black_friday?get_gift"))
        self.count = 0


sending_dec5_1 = SendingData("sending_dec5_1",
                             f"Вы просили - я сделала😌\n\nЧтобы Вы смогли изменить свою жизнь, я запустила бесплатный практикум \"Квантовый прорыв\".  Подготовимся к 2024 году, чтобы желания наконец стали сбываться, и вы смогли легко и уверенно жить жизнь.\n\nСейчас тот самый момент, когда пора стать тем, кем так хотелось. Сейчас или никогда❤️\n\nЖду вас здесь - https://t.me/+NzRieBzcMMYwNTE6",
                             url="https://t.me/+NzRieBzcMMYwNTE6",
                             btn_title="🥰 Перейти"
                             )
