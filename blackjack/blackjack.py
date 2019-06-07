import cards


def print_hand(hand):
    print("Your hand contains:")
    for rank, suit in hand:
        print(f" - {rank} of {suit}")
    print(f"Your score is {cards.calculate_hand_score(hand)}.")


def ask_user_to_hit_or_stand():
    """
    Ask a user if they want to hit or stand. If they give invalid
    input, continue asking.
    """

    while True:
        user_input = input("Do you want to (h)it or (s)tand? ").lower()
        if user_input in ("h", "s"):
            return user_input

        print("I don't understand that input. Try again.")


if __name__ == "__main__":
    deck = cards.create_deck(shuffle=True)
    hand = []

    hand.append(cards.get_card(deck))
    hand.append(cards.get_card(deck))

    bust = cards.calculate_hand_score(hand) > 21
    stand = False

    while not bust and not stand:
        print_hand(hand)
        hit_or_stand = ask_user_to_hit_or_stand()
        if hit_or_stand == "h":
            hand.append(cards.get_card(deck))
            bust = cards.calculate_hand_score(hand) > 21
        else:
            stand = True

    print_hand(hand)
    if bust:
        print("YA BUSTED!!!!!!!!")
