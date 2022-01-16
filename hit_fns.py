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

def hand_status(input_cards):
    """
    Checks to see if this hand has busted.

    Checks to see if any of the cards is a 10. Calculates the hand value and compares to 21.
    First time around, tries Ace as 11. If player busts with Ace as 11, repeat count with Ace as 1.
    """

    card_total = 0
    busted = False
    card_num = 0 # Track which card (1st, second, etc.)

    for card in input_cards:
        """
        For each card, there are four possibilities: 10, 1-9, Ace, or Face Card
        """
        is_ace = False

        if card[0] == 'A':
            result = ace_handler
        else:

        if len(card) == 3:  # Handle case in which card is the number 10 (card value has 2 digits).
            card_total += 10
        elif card[0] == 'A': # Handle cases in which card is a 1-9, Ace, or face card (card value has 1 digit).
            try: # Handle case in which card is 1-9.
                card_total += int(card[0])  # Throws error if card is an alpha character.
            except:
                if card[0] != 'A': # Check whether a non-Ace (face card).
                    card_total += 10
                else: # Handle case where card is an ace. Value is 11, will be changed if busting.
                    if card1_ace_1 == False:
                        card_total += 11
                    else:
                        card_total += 1

    if card_total > 21:
        busted = True
    else:
        pass
    return busted, card_total