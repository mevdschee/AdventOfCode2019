import os
import sys

fields = []
collisions = []
delta = {
    'U': (0,-1),
    'D': (0,1),
    'L': (-1,0),
    'R': (1,0),
}

dir = os.path.dirname(__file__)
with open(os.path.join(dir,"input")) as f:
    lines = []
    for line in f:
        directions = list(line.strip().split(','))
        field = {}
        x = 0
        y = 0
        for direction in directions:
            dx, dy = delta[direction[0]]
            steps = int(direction[1:])
            for i in range(steps):
                x += dx
                y += dy
                field[(x,y)] = True
        fields.append(field)
    for (x,y) in fields[0]:
        if (x,y) in fields[1]:
            collisions.append((x,y))
    best = sys.maxsize
    for c in collisions:
        best = min(best,abs(c[0])+abs(c[1]))
    print(best)