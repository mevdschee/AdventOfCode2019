import os
import json

dir = os.path.dirname(__file__)
with open(os.path.join(dir, "input")) as f:
    building_list, jump_list = list(json.loads(f.read()).values())
    buildings = dict(building_list)
    x, y = building_list[0]
    steps = 1
    for dx, dy in jump_list:
        x, y = x+1+dx, y+dy
        if not x in buildings:
            break
        if y < buildings[x]:
            break
        y = buildings[x]
        steps += 1
    print(steps)
    