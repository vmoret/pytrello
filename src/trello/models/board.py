from ..proxy import TrelloAPI
from ..immutable import Map, List
from .list import Lists
from .card import Cards


class Board(Map):

    __slots__ = ('data', '__lists', '__cards')

    def __eq__(self, other):
        if isinstance(other, str):
            return self['name'] == other
        return super().__eq__(other)

    @property
    def lists(self):
        try:
            return self.__lists
        except AttributeError:
            self.__lists = Lists('board/{:}/lists'.format(self['id']))
            return self.__lists

    @property
    def cards(self):
        try:
            return self.__cards
        except AttributeError:
            self.__cards = Cards('board/{:}/cards'.format(self['id']))
            return self.__cards

