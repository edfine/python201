from typing import Tuple

my_data: Tuple[str, int, float] = ("Dave", 10, 5.7)

from typing import List

# you can create aliases for types like this
DeckOfCards = List[Tuple[str, str]]

deck: DeckOfCards = [
    ('3', 'spades'),
    ('J', 'diamonds'),
    ('A', 'clubs'),
    (4, 'diamonds')
]
