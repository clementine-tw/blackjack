import unittest
from card import Card, CardNumber, new_deck_of_cards


class TestCard(unittest.TestCase):
    def test_card_number(self):
        card = Card(CardNumber.ACE)
        self.assertEqual(card.card_num, CardNumber.ACE)

    def test_card_side(self):
        card = Card(CardNumber.ACE)
        self.assertEqual(card.is_right_side, False)


class TestCardDeck(unittest.TestCase):
    def test_new_deck(self):
        deck = new_deck_of_cards()
        self.assertEqual(len(deck), 52)
