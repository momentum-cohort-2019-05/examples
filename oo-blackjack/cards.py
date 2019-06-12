import random

RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
SUITS = ("Spades", "Clubs", "Diamonds", "Hearts")
SUIT_SYMBOLS = {'Spades': "♠", 'Clubs': "♣", 'Diamonds': "♦", 'Hearts': "♥"}


class Card:

    def __init__(self, rank, suit):
        # Not necessary, but useful to prevent bad data.
        if rank not in RANKS:
            raise ValueError("Invalid rank")
        if suit not in SUITS:
            raise ValueError("Invalid suit")

        self.rank = rank
        self.suit = suit

    def get_value(self):
        """Return the card's blackjack value."""
        if self.rank == "A":
            return 1

        if self.rank in ("J", "Q", "K"):
            return 10

        return int(self.rank)

    def __str__(self):
        return f"{self.rank}{SUIT_SYMBOLS[self.suit]}"


class Deck:

    def __init__(self):
        self.cards = []
        for rank in RANKS:
            for suit in SUITS:
                self.cards.append(Card(rank, suit))

        # Functionally the same
        # self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


class Hand:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        total = sum([card.get_value() for card in self.cards])
        if total <= 11 and self.contains_rank("A"):
            total += 10
        return total

    def contains_rank(self, rank):
        return rank in [card.rank for card in self.cards]


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()
    print(deck.draw_card())
    print(deck.draw_card())

    my_hand = Hand()
    my_hand.add_card(Card("9", "Clubs"))
