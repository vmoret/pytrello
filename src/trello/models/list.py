from ..proxy import TrelloAPI
from ..immutable import Map, List as _List
from .card import Cards


class List(Map):

    __slots__ = ('data', '__cards')

    def __eq__(self, other):
        if isinstance(other, str):
            return self['name'] == other
        return super().__eq__(other)

    @property
    def cards(self):
        try:
            return self.__cards
        except AttributeError:
            self.__cards = Cards('lists/{:}/cards'.format(self['id']))
            return self.__cards


class Lists(_List):
    def __init__(self, url, **kwargs):
        super().__init__([List(x) for x in TrelloAPI().get(url, **kwargs)])

