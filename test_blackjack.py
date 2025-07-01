import unittest
from blackjack import Gamer, sum_points
from card import Card, CardNumber, CardDeck


class TestGamer(unittest.TestCase):
    def test_init_cards(self):
        gamer = Gamer(name="p", cards=CardDeck([Card(CardNumber.KING)]))
        self.assertEqual(gamer.card_deck.cards[0].card_num, CardNumber.KING)

    def test_add_card(self):
        gamer = Gamer(name="p", cards=CardDeck([Card(CardNumber.KING)]))
        gamer.add_card(Card(CardNumber.TWO))
        self.assertEqual(
            gamer.card_deck.cards, [Card(CardNumber.KING), Card(CardNumber.TWO)]
        )

    def test_sum_points(self):
        gamer = Gamer(
            name="p", cards=CardDeck([Card(CardNumber.KING), Card(CardNumber.TWO)])
        )

        want = 12
        got = sum_points(gamer.card_deck)
        self.assertEqual(got, want)

    def test_sum_points_8(self):
        gamer = Gamer(
            name="p",
            cards=CardDeck(
                [
                    Card(CardNumber.FIVE, True),
                    Card(CardNumber.THREE, True),
                ]
            ),
        )

        want = 8
        got = sum_points(gamer.card_deck)
        self.assertEqual(got, want)

    def test_sum_points_with_aces_small(self):
        gamer = Gamer(
            name="p",
            cards=CardDeck(
                [Card(CardNumber.KING), Card(CardNumber.TWO), Card(CardNumber.ACE)]
            ),
        )

        want = 13
        got = sum_points(gamer.card_deck)
        self.assertEqual(got, want)

    def test_sum_points_with_aces_big(self):
        gamer = Gamer(
            name="p",
            cards=CardDeck(
                [Card(CardNumber.TWO), Card(CardNumber.TWO), Card(CardNumber.ACE)]
            ),
        )

        want = 15
        got = sum_points(gamer.card_deck)
        self.assertEqual(got, want)

    def test_gamer_state(self):
        gamer = Gamer(
            name="p",
            cards=CardDeck(
                [
                    Card(CardNumber.FIVE, True),
                    Card(CardNumber.THREE, True),
                ]
            ),
        )

        want = "p  8  5  3 "
        got = gamer.state(is_show_points=True)
        self.assertEqual(got, want)
