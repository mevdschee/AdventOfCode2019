import os
import math

dir = os.path.dirname(__file__)
with open(os.path.join(dir, "input")) as f:
    field = []
    for line in f:
        field.append(list(line.strip()))
    w = len(field[0])
    h = len(field)
    asteroids = {}
    for y in range(h):
        for x in range(w):
            if field[y][x] == "#":
                asteroids[(x, y)] = True
    best_score = 0
    for sx, sy in asteroids:
        moves = {}
        for ty in range(h):
            for tx in range(w):
                dx, dy = tx - sx, ty - sy
                if (dx, dy) != (0, 0):
                    gcd = math.gcd(dx, dy)
                    dx //= gcd
                    dy //= gcd
                    moves[(dx, dy)] = True
        seen = 0
        for dx, dy in moves:
            for i in range(1, max(w, h)):
                x, y = sx + i * dx, sy + i * dy
                if x < 0 or y < 0 or x >= w or y >= h:
                    break
                if (x, y) in asteroids:
                    seen += 1
                    break
        if seen > best_score:
            best_score = seen
    print(best_score)
