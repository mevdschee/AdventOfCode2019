import os

dir = os.path.dirname(__file__)
with open(os.path.join(dir, "input")) as f:
    lines = f.read().strip().split("\n")
    deck = 119315717514047
    iterations = 101741582076661
    position = 2020
    
    a = 1
    b = 0
    for line in reversed(lines):
        text, number = line.rsplit(" ", 1)
        if text == "deal into new":
            a = (-a) % deck
            b = (deck - 1 - b) % deck
        elif text == "cut":
            b = (b + int(number)) % deck
        elif text == "deal with increment":
            inv = pow(int(number), deck - 2, deck)
            a = (a * inv) % deck
            b = (b * inv) % deck
    
    final_a = pow(a, iterations, deck)
    
    if a == 1:
        final_b = (b * iterations) % deck
    else:
        final_b = (b * (final_a - 1) % deck * pow(a - 1, deck - 2, deck)) % deck
    
    result = (final_a * position + final_b) % deck
    print(result)
