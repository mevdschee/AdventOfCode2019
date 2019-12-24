import os

dir = os.path.dirname(__file__)
with open(os.path.join(dir, "input")) as f:
    lines = f.read().rstrip().split("\n")
    width = len(lines[0])
    height = len(lines)
    directions = [(0, -1),(0, 1),(-1, 0),(1, 0)]
    states = {}
    while True:
        state = "\n".join(lines)
        if state in states:
            break
        states[state] = lines
        new_lines = ['']*height
        for y in range(height):
            for x in range(width):
                count = 0
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx<0 or ny<0 or nx>=width or ny>=height:
                        continue
                    if lines[ny][nx]=='#':
                        count += 1
                char = '.'
                if lines[y][x]=='#':
                    if count==1:
                        char='#'
                else:
                    if count==1 or count==2:
                        char='#'
                new_lines[y] += char
        lines = new_lines
    result = 0
    for y in range(height):
        for x in range(width):
            if lines[y][x]=='#':
                result += 2**(y*width+x)
    print(result)
    