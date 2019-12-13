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
        if mode==2:
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

field = {}
state = load("input")
state["mem"][0]=2
tiles = ["empty","wall","block","paddle","ball"]
inputs = {"left":-1,"neutral":0,"right":1}
input = 0
score = 0
ball_pos = 0
paddle_pos = 0
while True:
    blocks = 0
    while True:
        output = run(state,[input],3)
        if len(output)!=3:
            break
        x,y,tile = output[0],output[1],output[2]
        if x==-1 and y==0:
            score = tile
        elif tiles[tile]=="ball":
            ball_pos = x
            if ball_pos<paddle_pos:
                input = inputs["left"]
            elif ball_pos==paddle_pos:
                input = inputs["neutral"]
            elif ball_pos>paddle_pos:
                input = inputs["right"]
        elif tiles[tile]=="paddle":
            paddle_pos = x
        elif tiles[tile]=="block":
            blocks += 1
    if blocks == 0:
        break
print(score)
