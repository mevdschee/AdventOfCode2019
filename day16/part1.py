import os

pattern = [0, 1, 0, -1]

dir = os.path.dirname(__file__)
with open(os.path.join(dir, "input")) as f:
    line = f.read().strip()
    for _ in range(100):
        values = list(map(int,list(line)))
        new_line = ""
        for i in range(len(values)):
            total = 0
            for j in range(len(values)):
                value = values[j]
                multiplier = pattern[((j+1)//(i+1))%len(pattern)]
                total += value * multiplier
            new_line += str(total)[-1]
        line = new_line
    print(line[0:8])