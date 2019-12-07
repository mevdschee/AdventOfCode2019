import os

input = [5]
output = []

dir = os.path.dirname(__file__)
with open(os.path.join(dir, "input")) as f:
    mem = list(map(int, f.read().strip().split(',')))
    lengths = [4, 4, 2, 2, 3, 3, 4, 4]
    pc = 0
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
        jump = False
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
                jump = True
        elif operation == 6:
            if params[0] == 0:
                pc = params[1]
                jump = True
        elif operation == 7:
            mem[address] = int(params[0] < params[1])
        elif operation == 8:
            mem[address] = int(params[0] == params[1])
        if not jump:
            pc += length
    print(output)
