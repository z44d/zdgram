import html
import zdgram

class User:
    id: int
    is_bot: bool
    first_name: str
    last_name: str
    username: str
    language_code: str
    is_premium: str
    added_to_attachment_menu: bool
    can_join_groups: bool
    can_read_all_group_messages: bool
    supports_inline_queries: bool
    mention: "zdgram.types.Mention"
    link: str

    def _parse(self, dc: dict):
        dc['mention'] = {
            'markdown': '[{}](tg://user?id={})'.format(html.escape(dc['first_name']), str(dc['id'])),
            'html': '<a href="tg://user?id={}">{}</a>'.format(str(dc['id']), html.escape(dc['first_name']))
        }
        if dc.get('username'):
            dc['link']="http://t.me/{}".format(dc['username'])
        return dc