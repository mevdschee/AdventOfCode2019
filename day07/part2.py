import os
from itertools import permutations 

def load(program: str) -> dict:
    mem = []
    dir = os.path.dirname(__file__)
    with open(os.path.join(dir, program)) as f:
        mem = list(map(int, f.read().strip().split(',')))
    return {
        "mem": mem,
        "pc": 0,
    }
    
def run(state: dict, input: list) -> list:
    mem = state["mem"]
    pc = state["pc"]
    input.reverse()
    output = []
    lengths = [4, 4, 2, 2, 3, 3, 4, 4]
    while True:
        operation = mem[pc] % 100
        if operation == 99:
            break
        length = lengths[operation-1]
        address = mem[pc+length-1]
        params = mem[pc+1:pc+length]
        modes = mem[pc] // 100
        for i in range(len(params)):
            if modes % 10 == 0:
                params[i] = mem[params[i]]
            modes //= 10
        pc += length
        if operation == 1:
            mem[address] = params[0] + params[1]
        elif operation == 2:
            mem[address] = params[0] * params[1]
        elif operation == 3:
            mem[address] = input.pop()
        elif operation == 4:
            output.append(params[0])
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
    state["mem"] = mem
    state["pc"] = pc
    return output

best_output = -1
configs = permutations(range(5,10)) 
for config in configs:
    output = 0
    states = []
    for i in range(len(config)):
        states.append(load("input"))
        output_list = run(states[i],[config[i],output])
        if len(output_list) > 0:
            output = output_list[0]
    while len(output_list) > 0:
        for i in range(len(config)):
            output_list = run(states[i],[output])
            if len(output_list) > 0:
                output = output_list[0]
    if output>best_output:
        best_output = output
print(best_output)