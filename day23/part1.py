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
            if len(input) == 0:
                break
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


states = {}
messages = {}
result = -1
for i in range(50):
    states[i] = load("input")
    messages[i] = []
    run(states[i], [i], -1)
while result == -1:
    for i in range(50):
        outputs = []
        if len(messages[i]) > 0:
            outputs += run(states[i], messages[i], -1)
            messages[i] = []
        outputs += run(states[i], [-1], -1)
        for j in range(0, len(outputs), 3):
            t, x, y = outputs[j:j+3]
            if t == 255:
                result = y
                break
            messages[t] += [x, y]

print(result)
