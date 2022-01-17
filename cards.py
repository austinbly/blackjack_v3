
values = ['ace','2','3','4','5','6','7','8','9','10','j','q','k']
suits = ['hearts', 'diamonds', 'spades', 'clubs']
deck = []

for suit in suits:
    for value in values:
        deck.append(
            (value, suit)
        )

print(deck)