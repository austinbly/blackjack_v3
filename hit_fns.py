def player_hit(current_deck, player_cards):
    """
    Player hits.

    Gives the player a new card.
    """

    new_card = rand.choice(current_deck)
    player_cards.append(new_card)
    return (current_deck, player_cards)

def dealer_hit(current_deck, dealer_cards):
    """
    Dealer Hits.

    Gives the dealer a new card.
    """

    new_card = rand.choice(current_deck)
    dealer_cards.append(new_card)
    return (current_deck, dealer_cards)

def bust_checker(input_cards):
    """
        Checks to see if this hand has busted.

        Calculates the hand value and compares to 21.
    """
    card_total = 0  # initialize variable for card total
    bust = False
    for card in input_cards:
        if len(card) == 2:  # check if 2 digit or 3 digit
            try:
                card_total += int(card[0])
            except:  # if face card
                card_total += 10
        else:
            card_total += int(card[0] + card[1])
    if card_total > 21:
        bust = True
    else:
        bust = False
    return bust, card_total