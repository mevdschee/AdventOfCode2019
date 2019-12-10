import os
import math

dir = os.path.dirname(__file__)
with open(os.path.join(dir,"input")) as f:
    field = []
    for line in f:
        field.append(list(line.strip()))
    w = len(field[0])
    h = len(field)
    asteroids = {}
    for y in range(h):
        for x in range(w):
            if field[y][x]=='#':
                asteroids[(x,y)]=True
    scores = []
    for sx, sy in asteroids:
        moves = {}
        for ty in range(h):
            for tx in range(w):
                dx, dy = tx - sx, ty - sy
                gcd = math.gcd(dx,dy)
                if gcd > 0:
                    dx //= gcd
                    dy //= gcd
                moves[(dx,dy)] = True
        seen = 0
        for dx, dy in moves:
            for i in range(1,max(w,h)):
                px, py = sx+i*dx,sy+i*dy
                if px<0 or py<0 or px>=w or py>=h:
                    break
                if (px, py) in asteroids:
                    seen += 1
                    break
        scores.append(seen)
    print(max(scores)-1)