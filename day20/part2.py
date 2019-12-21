import os

def calculate_distances(field: dict, portals: dict, positions: dict) -> dict:
    result = {}
    for key, pos in positions.items():
        for x, y in pos:
            new_fronts = [(x, y)]
            visited = {(x, y): 0}
            directions = {"north": (0, -1), "south": (0, 1),
                        "west": (-1, 0), "east": (1, 0)}
            steps = 0
            while len(new_fronts) > 0:
                steps += 1
                fronts = new_fronts
                new_fronts = []
                for x, y in fronts:
                    for d in directions:
                        dx, dy = directions[d]
                        nx, ny = x + dx, y + dy
                        if (nx, ny) in field and not (nx, ny) in visited:
                            if field[(nx, ny)] == '.':
                                if (nx,ny) in portals and portals[(nx,ny)]!=key:
                                    nkey = portals[(nx,ny)]
                                    if not key in result:
                                        result[key] = {}
                                    if not nkey in result:
                                        result[nkey] = {}
                                    result[key][nkey] = steps
                                    result[nkey][key] = steps
                                visited[(nx, ny)] = True
                                new_fronts.append((nx, ny))
    return result

dir = os.path.dirname(__file__)
with open(os.path.join(dir, "input")) as f:
    lines = list(map(list, f.read().rstrip().split("\n")))
    width = len(lines[0])
    height = len(lines)
    field = {}
    portals = {}
    positions = {}
    directions = {"north": ((0, -2), (0, -1)), "south": ((0, 1),(0, 2)),
                  "west": ((-2, 0),(-1, 0)), "east": ((1, 0),(2, 0))}
    for y in range(height):
        for x in range(width):
            if x<len(lines[y]):
                k = lines[y][x]
                if k == '.' or k == '#':
                    field[(x, y)] = k
                if k == '.':
                    for d in directions:
                        dx1, dy1 = directions[d][0]
                        dx2, dy2 = directions[d][1]
                        c1,c2 = lines[y+dy1][x+dx1],lines[y+dy2][x+dx2]
                        if c1.isupper() and c2.isupper():
                            outer = x == 2 or y == 2 or x == width-3 or y == height-3
                            if outer:
                                label = 'o' + c1 + c2
                            else: 
                                label = 'i' + c1 + c2
                            portals[(x, y)] = label
                            if not label in positions:
                                positions[label] = []
                            positions[label].append((x,y))

    distances = calculate_distances(field, portals, positions)
    
    states = {}
    new_states = {'0,oAA':{
        "at": "oAA",
        "level": 0,
        "steps": 0,
        "path": 'AA',
    }}
    results = []
    step = 0
    while len(new_states) > 0 and len(results)<1:
        step += 1
        states = new_states
        new_states = {}
        for state in states.values():
            at = state["at"]
            level = state["level"]
            if at == 'iZZ' and level == -1:
                results.append(state)
            if at in distances and level>=0:
                for key, steps in distances[at].items():
                    if key[0:1]=='o':
                        new_level = level-1
                        new_at = 'i'+key[1:]
                    else:
                        new_level = level+1
                        new_at = 'o'+key[1:]
                    new_path = state["path"] + ',' + key[1:]
                    new_steps = state["steps"] + steps+1
                    index = ','.join([str(new_level),new_at])
                    if index in new_states and new_states[index]["steps"]<new_steps:
                        continue
                    new_states[index] = {
                        "at": new_at,
                        "level": new_level,
                        "steps": new_steps,
                        "path": new_path
                    }

    print(min(map(lambda s:s["steps"]-1,results)))