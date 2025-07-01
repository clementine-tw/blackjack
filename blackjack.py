import sys
import random
from card import Card, CardNumber, CardDeck, new_deck_of_cards


class Gamer:
    def __init__(self, name: str, cards: CardDeck):
        self.name = name
        self.card_deck = cards
        self.points = sum_points(self.card_deck)
        self.is_bomb = False

    def add_card(self, card: Card):
        self.card_deck.push(card)
        self.points = sum_points(self.card_deck)
        if self.points > MAX_POINT:
            self.is_bomb = True

    def turn_right_cards(self, index: int):
        if index >= len(self.card_deck.cards):
            return
        self.card_deck.cards[index].is_right_side = True

    def state(self, is_show_points=False) -> str:
        points_str = str(self.points).rjust(2, " ") if is_show_points else "**"
        bomb_str = "Bomb!" if self.is_bomb else ""
        return f"{self.name} {points_str} {self.card_deck} {bomb_str}"


def game():
    clear_terminal_ansi()
    new_game()


def new_game():

    cards = CardDeck(new_deck_of_cards())
    cards.shuffle()

    dealer = Gamer(name="Dealer", cards=CardDeck([cards.pop(True), cards.pop()]))
    player = Gamer(name="Player", cards=CardDeck([cards.pop(True), cards.pop(True)]))

    draw_game(dealer.state(), player.state(is_show_points=True))

    # Player rounds
    while True:
        choose = input("Y: continue, N:stop (Y/n) ")
        match choose.lower():
            case "n":
                break
            case _:
                player.add_card(cards.pop(True))
                draw_game(dealer.state(), player.state(is_show_points=True))
                if player.is_bomb:
                    break
    if player.is_bomb:
        print("Dealer Win!")
        return

    # Dealer rounds
    dealer.turn_right_cards(1)
    while True:
        choose = random.randint(0, 1)
        if choose == 0:
            dealer.add_card(cards.pop(True))
            draw_game(dealer.state(), player.state(is_show_points=True))
            if dealer.is_bomb:
                break
        else:
            break

    draw_game(dealer.state(is_show_points=True), player.state(is_show_points=True))

    if dealer.is_bomb:
        print("You Win!")
        return

    if player.points > dealer.points:
        print("You Win!")
    elif player.points < dealer.points:
        print("Dealer Win!")
    else:
        print("Deal!!!")


GAME_COL = 60


def format_line(content: str):
    pre = f"║ {content}"
    post = " ║"
    pad = GAME_COL - len(post)
    return pre.ljust(pad, " ") + post


def draw_game(dealer_state: str, player_state: str):
    clear_terminal_ansi()
    print("Welcome to Blackjack!")
    print("╔" + "═" * (GAME_COL - 2) + "╗")
    print(format_line(dealer_state))
    print(format_line(player_state))
    print("╚" + "═" * (GAME_COL - 2) + "╝")


def clear_terminal_up_line(lines: int):
    for _ in range(lines):
        sys.stdout.write("\033[A\033[K")
    sys.stdout.flush()


def clear_terminal_ansi():
    sys.stdout.write("\033[H\033[2J")
    sys.stdout.flush()


card_num_point_map = {
    CardNumber.TWO: 2,
    CardNumber.THREE: 3,
    CardNumber.FOUR: 4,
    CardNumber.FIVE: 5,
    CardNumber.SIX: 6,
    CardNumber.SEVEN: 7,
    CardNumber.EIGHT: 8,
    CardNumber.NINE: 9,
    CardNumber.TEN: 10,
    CardNumber.JACK: 10,
    CardNumber.QUEEN: 10,
    CardNumber.KING: 10,
}

MAX_POINT = 21


def sum_points(cards: CardDeck):
    aces = 0
    sum = 0
    for card in cards:
        # ACE can be worth either 1 or 11, depending on what benefits
        # the player's hand the most.
        if card.card_num == CardNumber.ACE:
            aces += 1
            continue
        sum += card_num_point_map[card.card_num]

    if aces == 0:
        return sum

    sum_big = sum + 11 + aces - 1
    sum_small = sum + aces
    return sum_big if sum_big <= MAX_POINT else sum_small
