import random as rand

def new_deck():
    """Creates a new desk of cards"""

    deck = [] # stores deck during assembly
    cards = list(range(2,9,1))+['10','J','Q','K','A']
    suits = ['D','H','S','C']
    # assemble deck
    for suit in suits:
        for card in cards:
            new_card = str(card)+suit
            deck.append(new_card)
    return deck

def deal_cards(current_deck):
    """Deals cards to player and dealer."""

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

