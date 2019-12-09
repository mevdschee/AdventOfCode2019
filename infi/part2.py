import os
import sys
import json


def step(energy: int, building_list: list) -> int:
    if len(building_list) == 1:
        return energy
    buildings = dict(building_list)
    scores = []
    x, y = building_list[0]
    for dx in range(5):
        nx = x + 1 + dx
        if nx in buildings:
            dy = max(0, buildings[nx] - y)
            if dx + dy <= 4:
                de = dx + max(0, dy)
                i = building_list.index([nx,buildings[nx]])
                scores.append(step(energy+de, building_list[i:]))
    if len(scores) == 0:
        return sys.maxsize
    return min(scores)

dir = os.path.dirname(__file__)
with open(os.path.join(dir, "input")) as f:
    print(step(0, list(json.loads(f.read()).values())[0]))
