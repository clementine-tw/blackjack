import random
from enum import Enum


class CardNumber(Enum):
    ACE = "A"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"
    QUEEN = "Q"
    KING = "K"


class Card:
    def __init__(self, card_num: CardNumber, is_right_side: bool = False):
        self.card_num = card_num
        self.is_right_side = is_right_side

    def __repr__(self):
        return f"{self.card_num}"

    def __str__(self):
        s = f"{self.card_num.value}" if self.is_right_side else "*"
        return s.rjust(2, " ")

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        if self.card_num != other.card_num:
            return False
        return True


class CardDeck:
    def __init__(self, init_cards: list[Card] = []):
        self.cards = init_cards

    def __iter__(self):
        for card in self.cards:
            yield card

    def shuffle(self):
        random.shuffle(self.cards)

    def pop(self, is_right_side=False) -> Card:
        card = self.cards.pop()
        card.is_right_side = is_right_side
        return card

    def push(self, card: Card):
        self.cards.append(card)

    def __str__(self):
        return " ".join(list(map(lambda c: str(c), self.cards)))


def new_deck_of_cards() -> list[Card]:
    cards = []
    for number in CardNumber:
        for _ in range(4):
            cards.append(Card(number))
    return cards
