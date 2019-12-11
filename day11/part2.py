import os

def load(program: str) -> dict:
    mem = []
    dir = os.path.dirname(__file__)
    with open(os.path.join(dir, program)) as f:
        mem = list(map(int, f.read().strip().split(',')))
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
    input.reverse()
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
        if mode==2:
            address += base
        pc += length
        if operation == 1:
            mem[address] = params[0] + params[1]
        elif operation == 2:
            mem[address] = params[0] * params[1]
        elif operation == 3:
            mem[address] = input.pop()
        elif operation == 4:
            output.append(params[0])
            if len(output)==read:
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

field = {(0,0):1}
pos = (0,0)
directions = [(0,-1),(1,0),(0,1),(-1,0)]
dir = 0
state = load("input")
while True:
    color = 0
    if pos in field:
        color = field[pos]
    output = run(state,[color],2)
    if len(output)!=2:
        break
    if output[0]:
        field[pos] = output[0]
    if output[1]==1:
        dir += 1
    else:
        dir -= 1
    dir %= len(directions)
    pos = tuple(map(sum, zip(pos, directions[dir])))

width = max(field.keys(),key=lambda i:i[0])[0]
height = max(field.keys(),key=lambda i:i[1])[1]
for y in range(height+1):
    for x in range(1,width+1):
        if (x,y) in field:
            c = '#'
        else:
            c = ' '
        print(c, end='')
    print()
