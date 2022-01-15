'''
Fn to create new deck
    -no inputs to call
    -outputs new list of cards
'''
def new_deck():

    deck = [] # stores deck during assembly
    cards = list(range(2,9,1))+['10','J','Q','K','A']
    suits = ['D','H','S','C']
    # assemble deck
    for suit in suits:
        for card in cards:
            new_card = str(card)+suit
            deck.append(new_card)
    return deck
