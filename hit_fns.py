import random as rand

def player_hit(current_deck, player_cards):
    """Give the player a random new card from the deck and take that card out of the deck."""

    new_card = rand.choice(current_deck)
    player_cards.append(new_card)
    current_deck.remove(new_card)
    return (current_deck, player_cards)

def dealer_hit(current_deck, dealer_cards):
    """Give the dealer a random new card from the deck and take that card out of the deck."""

    new_card = rand.choice(current_deck)
    dealer_cards.append(new_card)
    current_deck.remove(new_card)
    return (current_deck, dealer_cards)