from .proxy import TrelloAPI
from .models import *


class Trello(object):
    __slots__ = ()

    def __init__(self, key, token):
        api = TrelloAPI(key, token)
        super().__init__()

    def __getitem__(self, key):
        dto = TrelloAPI().get('boards/{:}'.format(key))
        return Board(dto)

