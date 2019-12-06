import os

input = [1]

dir = os.path.dirname(__file__)
with open(os.path.join(dir,"input")) as f:
    mem = list(map(int, f.read().strip().split(',')))
    lengths = [4,4,2,2]
    pc = 0
    while True:
        l = lengths[mem[pc]-1]
        operation,a,b,address = mem[pc:pc+4]
        result = 0
        if operation==1:
            result = mem[a]+mem[b]
        elif operation==2:
            result = mem[a]*mem[b]
        elif operation==3:
            result = input.pop()
        elif operation==4:
            result = mem[a]*mem[b]
        mem[address] = result
        pc+=4
    print(mem[0])