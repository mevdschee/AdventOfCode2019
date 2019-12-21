import os

def calculate_distances(field: dict, key_positions: list) -> dict:
    result = {}
    for key, position in key_positions.items():
        result[key] = {}
        x, y = position
        new_fronts = [(x, y, [])]
        visited = {(x, y): 0}
        directions = {"north": (0, -1), "south": (0, 1),
                    "west": (-1, 0), "east": (1, 0)}
        steps = 0
        while len(new_fronts) > 0:
            steps += 1
            fronts = new_fronts
            new_fronts = []
            for x, y, keys in fronts:
                for d in directions:
                    dx, dy = directions[d]
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in field and not (nx, ny) in visited:
                        if field[(nx, ny)] != '#':
                            k = field[(nx, ny)]
                            nkeys = keys
                            if k.isupper() and not k.lower() in keys:
                                nkeys = keys + [k.lower()]
                            if k.islower() and not k in keys:
                                result[key][k] = (steps,nkeys)
                            visited[(nx, ny)] = True
                            new_fronts.append((nx, ny, nkeys))
    return result

dir = os.path.dirname(__file__)
with open(os.path.join(dir, "input")) as f:
    lines = list(map(list, f.read().strip().split("\n")))
    width = len(lines[0])
    height = len(lines)
    key_positions = {}
    field = {}
    for y in range(height):
        for x in range(width):
            k = field[(x, y)] = lines[y][x]
            if k == '@' or k.islower():
                key_positions[k] = (x, y)
    start_positions = [(-1,-1),(+1,-1),(-1,+1),(+1,+1)]
    x, y = key_positions['@']
    del key_positions['@']
    for px in range(-1,2):
        for py in range(-1,2):
            field[(x+px,y+py)] = '#'
    for i in range(len(start_positions)):
        px, py = start_positions[i]
        field[(x+px,y+py)] = str(i)
        key_positions[str(i)] = (x+px,y+py)
    distances = calculate_distances(field, key_positions)
    print(distances)
    states = {}
    new_states = {'0123':{
        "at": "0123",
        "steps": 0,
        "keys": []
    }}
    while len(new_states) > 0:
        states = new_states
        new_states = {}
        for state in states.values():
            for i in range(len(state["at"])):
                at = state["at"][i]
                for key, (steps, keys) in distances[at].items():
                    if not key in state["keys"] and len(set(keys) - set(state["keys"]))==0:
                        new_at = state["at"][:i] + key + state["at"][i+1:]
                        new_keys = state["keys"] + [key]
                        index = new_at+''.join(sorted(new_keys))
                        new_steps = state["steps"] + steps
                        if index in new_states and new_states[index]["steps"]<new_steps:
                            continue
                        new_states[index] = {
                            "at": new_at,
                            "steps": new_steps,
                            "keys": new_keys
                        }
    print(min(map(lambda s:s["steps"],states.values())))