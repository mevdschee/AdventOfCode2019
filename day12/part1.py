import os

dir = os.path.dirname(__file__)
with open(os.path.join(dir, "input")) as f:
    moons = []
    keys = ["x","y","z"]
    for line in f:
        pairs = line.strip().strip('<>').split(', ')
        moon = map(lambda s: (s.split('=')[0], int(s.split('=')[1])), pairs)
        moons.append({"pos": dict(moon), "vel": dict(zip(keys,[0,0,0]))})
    for step in range(1000):
        for m1 in moons:
            for m2 in moons:
                if m1 != m2:
                    for k in m1["pos"].keys():
                        if m1["pos"][k]<m2["pos"][k]:
                            m1["vel"][k]+=1
                        if m1["pos"][k]>m2["pos"][k]:
                            m1["vel"][k]-=1
        for m in moons:
            for k in m1["pos"].keys():
                m["pos"][k]+=m["vel"][k]
        print(step+1)
        for m in moons:
            print(m)
        print()
    energy = 0
    for m in moons:
        pos = sum(map(abs, m["pos"].values())) 
        vel = sum(map(abs, m["vel"].values()))
        energy += pos * vel
    print(energy)
