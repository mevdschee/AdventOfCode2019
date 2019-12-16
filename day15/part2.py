import os


def load(program: str) -> dict:
    mem = []
    dir = os.path.dirname(__file__)
    with open(os.path.join(dir, program)) as f:
        mem = list(map(int, f.read().strip().split(",")))
        mem += [0]*(4096-len(mem))
    return {
        "mem": mem,
        "pc": 0,
        "base": 0,
    }


def run(state: dict, input: list, read: int) -> list:
    mem = state["mem"]
    pc = state["pc"]
    base = state["base"]
    output = []
    lengths = [4, 4, 2, 2, 3, 3, 4, 4, 2]
    while True:
        operation = mem[pc] % 100
        if operation == 99:
            break
        length = lengths[operation-1]
        address = mem[pc+length-1]
        params = mem[pc+1:pc+length]
        modes = mem[pc] // 100
        mode = 0
        for i in range(len(params)):
            mode = modes % 10
            if mode == 0:
                params[i] = mem[params[i]]
            elif mode == 2:
                params[i] = mem[base+params[i]]
            modes //= 10
        address = mem[pc+length-1]
        if mode == 2:
            address += base
        pc += length
        if operation == 1:
            mem[address] = params[0] + params[1]
        elif operation == 2:
            mem[address] = params[0] * params[1]
        elif operation == 3:
            input.reverse()
            mem[address] = input.pop()
            input.reverse()
        elif operation == 4:
            output.append(params[0])
            if len(output) == read:
                break
        elif operation == 5:
            if params[0] != 0:
                pc = params[1]
        elif operation == 6:
            if params[0] == 0:
                pc = params[1]
        elif operation == 7:
            mem[address] = int(params[0] < params[1])
        elif operation == 8:
            mem[address] = int(params[0] == params[1])
        elif operation == 9:
            base += params[0]
    state["mem"] = mem
    state["pc"] = pc
    state["base"] = base
    return output


field = {}
state = load("input")
outputs = ["wall", "hallway", "goal"]
inputs = {"north": 1, "south": 2, "west": 3, "east": 4}
directions = {"north": (0, -1), "south": (0, 1),
              "west": (-1, 0), "east": (1, 0)}
x, y = goal = (0, 0)
path = []
while True:
    input = 0
    back = False
    nx, ny = x, y
    for d in directions:
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if not (nx, ny) in field:
            input = inputs[d]
            break
    if input == 0:
        if len(path) == 0:
            break
        back = True
        nx, ny = path.pop()
        dx, dy = nx-x, ny - y
        for d in directions:
            if directions[d] == (dx, dy):
                input = inputs[d]
                break
    output = run(state, [input], 1)[0]
    field[(nx, ny)] = output
    if outputs[output] != "wall":
        if outputs[output] == "goal":
            goal = (nx, ny)
        if not back:
            path.append((x, y))
        x, y = nx, ny

minx = min([i[0] for i in field.keys()])
maxx = max([i[0] for i in field.keys()])
miny = min([i[1] for i in field.keys()])
maxy = max([i[1] for i in field.keys()])

fronts = [goal]
distances = {}
distance = 0

while len(fronts) > 0:
    next_fronts = []
    for x, y in fronts:
        distances[(x, y)] = distance
        for d in directions:
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
            if field[(nx, ny)] != outputs.index("wall"):
                if not (nx, ny) in distances:
                    next_fronts.append((nx, ny))
    fronts = next_fronts
    distance += 1

print(max(distances.values()))
