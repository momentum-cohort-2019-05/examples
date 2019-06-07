import random

RANKS = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
SUITS = ("Spades", "Clubs", "Diamonds", "Hearts")


def create_deck(shuffle=False):
    """Create a deck of 52 cards."""
    deck = []
    for rank in RANKS:
        for suit in SUITS:
            deck.append((rank, suit))
    if shuffle:
        shuffle_deck(deck)
    return deck


def shuffle_deck(deck):
    """Given a deck, shuffle it."""
    random.shuffle(deck)
    return deck


def get_card(deck):
    return deck.pop()


def get_card_value(card):
    """Given a card (a tuple with rank and suit), return its value."""
    rank, suit = card
    if rank == "A":
        return 1

    if rank in ("J", "Q", "K"):
        return 10

    return int(rank)


def calculate_hand_score(hand):
    """
    Given a hand of cards (a list with card tuples), calculate the hand's score.

    How to calculate score:
    - Sum the value of each card together
    - If the sum is <= 11 and the hand has an ace in it, add 10 to score.
    """

    total = sum([get_card_value(card) for card in hand])
    if total <= 11 and does_hand_have_ace(hand):
        total += 10
    return total


def does_hand_have_ace(hand):
    """Given a hand of cards, return whether it has an ace in it."""
    for card in hand:
        rank = card[0]
        suit = card[1]
        if rank == "A":
            return True

    return False


if __name__ == "__main__":
    deck = create_deck()
    shuffle_deck(deck)
    print(deck)
    print(len(deck))
    print("Value of A", get_card_value(("A", "Spades")))
    print("Value of 9", get_card_value(("9", "Frogs")))
    print("Value of Q", get_card_value(("Q", "England")))

    hand = [
        ("2", "Hearts"),
        ("9", "Diamonds"),
        ("Q", "Spades"),
    ]
    print(hand)
    print("Score:", calculate_hand_score(hand))

    hand = [
        ("A", "Hearts"),
        ("7", "Diamonds"),
    ]
    print(hand)
    print("Score:", calculate_hand_score(hand))

    hand = [
        ("A", "Hearts"),
        ("A", "Hearts"),
        ("A", "Hearts"),
        ("7", "Diamonds"),
    ]
    print(hand)
    print("Score:", calculate_hand_score(hand))
