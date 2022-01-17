
def show_player_cards(cards):
    """Prints out player cards"""

    print('Player Cards are: ',end='')
    i = 1
    for card in cards:
        if i < len(cards):
            print(
                card[0].upper() + ' OF ' + card[1].upper(),end=', '
            )
        else:
            print(
                card[0].upper() + ' OF ' + card[1].upper()
            )
        i+=1


def show_dealer_cards(cards, show_dealer):
    """Prints out dealer cards"""

    if show_dealer == False: # If the dealer is only showing 1 card
        print('Dealer is showing: ', end='')
        i = 0
        for card in cards:
            if i == 0: # Skip the first card.
               pass
            elif i < len(cards)-1: # Do this for all except the last card.
                print(
                    card[0].upper() + ' OF ' + card[1].upper(),end=', '
                )
            else: # Do this for the last card.
                print(
                    card[0].upper() + ' OF ' + card[1].upper()
                )
            i+=1
    else: # If dealer is ready to show all cards
        print('Dealer cards are: ', end='')
        i = 0
        for card in cards:
            if i < len(cards) - 1:  # Do this for all except the last card.
                print(
                    card[0].upper() + ' OF ' + card[1].upper(), end=', '
                )
            else:  # Do this for the last card.
                print(
                    card[0].upper() + ' OF ' + card[1].upper()
                )
            i += 1