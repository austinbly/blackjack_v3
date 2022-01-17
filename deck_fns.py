import random as rand

def new_deck():
    """
    Creates a new shuffled deck of cards

    The cards are tuples.
    """

    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k']
    deck = []

    for suit in suits:
        for value in values:
            deck.append(
                (value, suit)
            )
    rand.shuffle(deck)
    return deck


def deal_cards(current_deck):
    """
    Deals cards to player and dealer.

    Input is a list of tuples of the format [('card 1 value','card 1 suit'), ('card 2 value', 'card 2 suit', etc.)...]
    """

    player_card_1 = rand.choice(current_deck)
    current_deck.remove(player_card_1)

    player_card_2 = rand.choice(current_deck)
    current_deck.remove(player_card_2)

    dealer_card_1 = rand.choice(current_deck)
    current_deck.remove(dealer_card_1)

    dealer_card_2 = rand.choice(current_deck)
    current_deck.remove(dealer_card_2)

    player_cards = [player_card_1, player_card_2]
    dealer_cards = [dealer_card_1, dealer_card_2]

    return (player_cards, dealer_cards, current_deck)