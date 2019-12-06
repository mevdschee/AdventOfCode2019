import os

for noun in range(100):
    for verb in range(100):
        dir = os.path.dirname(__file__)
        with open(os.path.join(dir,"input")) as f:
            mem = list(map(int, f.read().strip().split(',')))
            mem[1]=noun
            mem[2]=verb
            pc = 0
            while pc+4<len(mem):
                operation,a,b,address = mem[pc:pc+4]
                result = 0
                if operation==1:
                    result = mem[a]+mem[b]
                elif operation==2:
                    result = mem[a]*mem[b]
                mem[address] = result
                pc+=4
            if mem[0] == 19690720:
                print(100*noun+verb)
                exit()


