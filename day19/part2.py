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


first_col = 3
last_col = 4
first_cols = {}
last_cols = {}
y = 5
while True:
    state = load("input")
    output = run(state, [first_col,y], -1)[0]
    if output==0:
        first_col+=1
    state = load("input")
    output = run(state, [last_col,y], -1)[0]
    if output==1:
        last_col+=1
    first_cols[y%100] = first_col
    last_cols[y%100] = last_col
    if min(last_cols.values()) - max(first_cols.values()) >=100:
        break
    y+=1

px = min(last_cols.values())-100-1
py = y - 100

# width = 200
# height = 102
# total = 0
# for y in range(py-1,py+height):
#     for x in range(px-1,px+width):
#         state = load("input")
#         output = run(state, [x,y], -1)[0]
#         if output==1:
#             print('#',end='')
#         else:
#             print('.',end='')
#     print()

print(px*10000+py)