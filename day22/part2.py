import os


dir = os.path.dirname(__file__)
with open(os.path.join(dir, "test4")) as f:
    lines = f.read().strip().split("\n")
    deck = 10
    mul = 1
    add = 0
    for line in lines:
        text, number = line.rsplit(' ', 1)
        if text == "deal into new":
            mul *= -1
            add += mul
        if text == "cut":
            add += int(number) * mul
        if text == "deal with increment":
            mul *= int(number)**(deck-3)
        mul %= deck
        add %= deck
    for pos in range(deck):
        print((pos*mul+add) % deck, end=' ')
    print()

    # Cant solve this.. :-(
