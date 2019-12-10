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
    best_position = (0, 0)
    best_moves = {}
    for sx, sy in asteroids:
        moves = {}
        for ty in range(h):
            for tx in range(w):
                dx, dy = tx - sx, ty - sy
                if (dx, dy) != (0, 0):
                    gcd = math.gcd(dx, dy)
                    dx //= gcd
                    dy //= gcd
                    angle = math.degrees(math.atan2(dx, -dy))
                    if angle < 0:
                        angle += 360
                    moves[(dx, dy)] = angle
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
            best_position = (sx, sy)
            best_moves = moves

    clockwise_moves = [k for k, v in sorted(best_moves.items(), key=lambda i: i[1])]
    sx, sy = best_position
    shot = 0
    for dx, dy in clockwise_moves:
        for i in range(1, max(w, h)):
            x, y = sx + i * dx, sy + i * dy
            if x < 0 or y < 0 or x >= w or y >= h:
                break
            if (x, y) in asteroids:
                shot += 1
                if shot == 200:
                    print(x * 100 + y)
                    exit()
                break
