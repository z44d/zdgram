from typing import Union, List
from .parser import Parser

import zdgram

class InlineKeyboardMarkup(
    Parser
):
    def __init__(
        self,
        inline_keyboard: List[List["InlineKeyboardButton"]]
    ) -> None:
        super().__init__()
        self.inline_keyboard = inline_keyboard

    @property
    def get_json(self):
        data = {"inline_keyboard": []}
        for i in self.inline_keyboard:
            data["inline_keyboard"].append([x.__default__(x) for x in i])
        return data

class InlineKeyboardButton(
    Parser
):
    def __init__(
        self,
        text: str,
        url: str = None,
        callback_data: str = None,
        user_id: int = None,
        web_app: "zdgram.types.WebAppInfo" =None,
        login_url: "zdgram.types.LoginUrl" = None,
        switch_inline_query: str = None,
        switch_inline_query_current_chat: str = None,
        switch_inline_query_chosen_chat: "zdgram.types.SwitchInlineQueryChosenChat" = None,
        callback_game: "zdgram.types.CallbackGame" = None,
        pay: bool = None
    ) -> None:
        super().__init__()
        self.text = text
        if url: self.url = url
        if callback_data: self.callback_data = callback_data
        if web_app: self.web_app = web_app
        if login_url: self.login_url = login_url
        if switch_inline_query: self.switch_inline_query = switch_inline_query
        if switch_inline_query_current_chat: self.switch_inline_query_current_chat = switch_inline_query_current_chat
        if switch_inline_query_chosen_chat: self.switch_inline_query_chosen_chat = switch_inline_query_chosen_chat
        if callback_game: self.callback_game = callback_game
        if pay: self.pay = pay
        if user_id: self.url = f"tg://user?id={user_id}"
