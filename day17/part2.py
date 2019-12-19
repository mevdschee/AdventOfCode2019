import os
import re


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


state = load("input")
output = run(state, [], -1)
lines = ''.join(map(chr, output)).strip().splitlines()
width = len(lines[0])
height = len(lines)
field = {}
start = (0, 0)
for y in range(height):
    for x in range(width):
        if lines[y][x] == '^':
            start = (x, y)
        field[(x, y)] = lines[y][x]

directions = {"north": (0, -1), "south": (0, 1),
              "west": (-1, 0), "east": (1, 0)}
turns = ["north", "west", "south", "east"]
direction = "north"
visited = {}
path = []
x, y = start
while True:
    length = 0
    for d in directions:
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if (nx, ny) in visited:
            continue
        if (nx, ny) in field and field[(nx, ny)] == '#':
            if turns[turns.index(direction)-len(turns)+1]==d:
                turn = 'L'
            if turns[turns.index(direction)-1]==d:
                turn = 'R'
            direction = d
            break
    while True:
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy
        if (nx, ny) in field and field[(nx, ny)] == '#':
            x, y = nx, ny
            visited[(x, y)] = True
            length += 1
        else:
            break
    if length==0:
        break
    path += (turn,length)

path_str = ','.join(list(map(str,path)))

def find_programs(path_str: str, programs: str="", slot:int=0)-> list:
    if slot == 3:
        if len(path_str)>20:
            return []
        for program in programs.split("\n"):
            if len(program)>20:
                return []
        return [path_str+"\n"+programs]
    results = []
    for l in range(1,4):
        program = re.findall('([LR],[0-9]+(,[LR],[0-9]+){'+str(l)+'})', path_str)[0][0]
        results += find_programs(path_str.replace(program, chr(ord("A")+slot)),programs+program+"\n",slot+1)
    return results

path_str = find_programs(path_str)[0]
state = load("input")
input = list(map(ord,list(path_str+"n\n")))
state["mem"][0]=2
output = run(state, input, -1)
print(output[-1])
