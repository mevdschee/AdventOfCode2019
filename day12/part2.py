import os
from math import gcd

dir = os.path.dirname(__file__)
with open(os.path.join(dir, "input")) as f:
    moons = []
    keys = ["x","y","z"]
    for line in f:
        pairs = line.strip().strip('<>').split(', ')
        moon = map(lambda s: (s.split('=')[0], int(s.split('=')[1])), pairs)
        moons.append({"pos": dict(moon), "vel": dict(zip(keys,[0,0,0]))})
    firsts = {}
    cycles = {}
    for k in keys:
        firsts[k] = [m["pos"][k] for m in moons]
    steps = 0
    while len(cycles) < len(keys):
        steps += 1                    
        for m1 in moons:
            for m2 in moons:
                for k in keys:
                    if m1["pos"][k]<m2["pos"][k]:
                        m1["vel"][k]+=1
                    if m1["pos"][k]>m2["pos"][k]:
                        m1["vel"][k]-=1
        for m in moons:
            for k in keys:
                m["pos"][k]+=m["vel"][k]
        for k in keys:
            if not k in cycles:
                vel = [m["vel"][k] for m in moons]
                if vel == [0] * len(moons):
                    pos = [m["pos"][k] for m in moons]
                    if pos == firsts[k]:
                        cycles[k] = steps

a = list(cycles.values())
lcm = a[0]
for i in a[1:]:
    lcm = int(lcm*i/gcd(lcm, i))
print(lcm)