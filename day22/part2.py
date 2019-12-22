import os


dir = os.path.dirname(__file__)
with open(os.path.join(dir, "test4")) as f:
    lines = f.read().strip().split("\n")
    deck = 10
    mul = 1
    add = 0
    for line in lines:
        parts = line.rsplit(' ', 1)
        if parts[0] == "deal into new":
            mul *= -1
            add += mul
        if parts[0] == "cut":
            add += int(parts[1]) * mul
        if parts[0] == "deal with increment":
            mul *= int(parts[1])**(deck-3)
        mul %= deck
        add %= deck
    for pos in range(deck):
        print((pos*mul+add)%deck, end=' ')
    print()

    # Cant solve this.. :-(