import os


dir = os.path.dirname(__file__)
with open(os.path.join(dir, "input")) as f:
    lines = f.read().strip().split("\n")
    deck = list(range(10007))
    for line in lines:
        parts = line.rsplit(' ', 1)
        text = parts[0]
        if parts[1] == 'stack':
            parts[1] = '0'
        number = int(parts[1])
        new_deck = []
        if text == "deal into new":
            new_deck = list(reversed(deck))
        if text == "cut":
            new_deck = deck[number:] + deck[:number]
        if text == "deal with increment":
            new_deck = [-1]*len(deck)
            for i in range(len(deck)):
                new_deck[i*number % len(deck)] = deck[i]
        deck = new_deck

    print(deck.index(2019))
