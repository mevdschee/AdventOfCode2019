import os

def run(program: str,input: list) -> list:
    input.reverse()
    output = []
    dir = os.path.dirname(__file__)
    with open(os.path.join(dir, program)) as f:
        mem = list(map(int, f.read().strip().split(',')))
        mem += [0]*(4096-len(mem))
        lengths = [4, 4, 2, 2, 3, 3, 4, 4, 2]
        pc = 0
        base = 0
        while True:
            operation = mem[pc] % 100
            if operation == 99:
                break
            length = lengths[operation-1]
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
    return output

print(run("input",[2])[0])