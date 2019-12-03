import os
import sys

dir = os.path.dirname(__file__)
with open(os.path.join(dir,"test")) as f:
    lines = []
    for line in f:
        directions = list(line.strip().split(','))
        x = 0
        y = 0
        hor = []
        ver = []
        for direction in directions:
            dir = direction[0]
            steps = int(direction[1:])
            if dir=='U':
                ny=y-steps
                ver.append((x,(ny,y)))
            elif dir=='D':
                ny=y+steps
                ver.append((x,(y,ny)))
            elif dir=='L':
                nx=x-steps
                hor.append(((nx,x),y))
            elif dir=='R':
                nx=x+steps
                hor.append(((x,nx),y))
        lines.append((hor,ver))
    collisions = []
    for l in lines:
        print(l)
        for h in l[0][0]:
            for v in l[1][1]:
                if v[0]>h[0][0] and v[0]<h[0][1] and h[1]>v[1][0] and h[1]<v[1][1]:
                    collisions.append(v[0],h[1])
        for h in l[1][0]:
            for v in l[0][1]:
                if v[0]>h[0][0] and v[0]<h[0][1] and h[1]>v[1][0] and h[1]<v[1][1]:
                    collisions.append(v[0],h[1])
    best = sys.maxsize
    for c in collisions:
        best  = min(best,abs(c[0])+abs(c[1]))
    print(best)