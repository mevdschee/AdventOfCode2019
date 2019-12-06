import os

dir = os.path.dirname(__file__)
with open(os.path.join(dir,"input")) as f:
    mem = list(map(int, f.read().strip().split(',')))
    mem[1]=12
    mem[2]=2
    pc = 0
    while True:
        operation,a,b,address = mem[pc:pc+4]
        if operation==99:
            break
        result = 0
        if operation==1:
            result = mem[a]+mem[b]
        elif operation==2:
            result = mem[a]*mem[b]
        mem[address] = result
        pc+=4
    print(mem[0])

