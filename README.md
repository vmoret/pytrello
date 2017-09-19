# pytrello
Lightweight Trello python client

## Installation

Install the python distribution with `pip`.

```bash
pip install git+https://github.com/vmoret/pytrello.git
```

## Usage

```python
from trello import Trello, NewCard

cards = Trello('<Your API key>', '<Your auth token>')

# print cards
print(cards)

# add new card
cards.append(NewCard('do nothing', '<Your board ID>', labels=['Green']))
```

