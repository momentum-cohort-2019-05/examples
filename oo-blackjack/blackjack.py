from cards import Hand, Deck


class Dealer:

    def __init__(self):
        self.hand = Hand()
        self.deck = Deck()
        self.deck.shuffle()

    def deal_card(self, player):
        player.take_card(self.deck.draw_card())

    def take_card(self, card):
        self.hand.add_card(card)

    def will_hit(self):
        return self.hand.get_value() < 17


class Player:

    def __init__(self):
        self.hand = Hand()

    def take_card(self, card):
        self.hand.add_card(card)

    def will_hit(self):
        if self.hand.get_value() >= 21:
            return False

        print(f"Your current hand is: {self.hand}.")

        hit_or_stand = None
        while hit_or_stand is None or hit_or_stand.lower()[0] not in ['h', 's']:
            hit_or_stand = input("Do you want to (h)it or (s)tand? ")
        return hit_or_stand.lower()[0] == 'h'
