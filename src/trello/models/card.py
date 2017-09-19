from ..proxy import TrelloAPI
from ..immutable import Map, List


class Card(Map):
    def __eq__(self, other):
        if isinstance(other, str):
            return self['name'] == other
        return super().__eq__(other)


class NewCard(Card):
    def __init__(self, name, list_id, **kwargs):
        super().__init__(dict(name=name, idList=list_id, **kwargs))


class Cards(List):

    def __init__(self, url, **kwargs):
        super().__init__([Card(x) for x in TrelloAPI().get(url, **kwargs)])

    def append(self, card):
        dto = TrelloAPI().post('cards', card)
        return self.data.append(Card(dto))

