import os

pattern = [0, 1, 0, -1]

dir = os.path.dirname(__file__)
with open(os.path.join(dir, "input")) as f:
    line = f.read().strip()*10000
    offset = int(line[:7])
    line = line[offset:]
    values = list(map(int,list(line)))
    for _ in range(100):
        total = 0
        for i in range(len(values) - 1, -1, -1):
            total += values[i]
            values[i] = total%10
    print(''.join(map(str,values[0:8])))