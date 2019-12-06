import os

root = False

dir = os.path.dirname(__file__)
with open(os.path.join(dir,"input")) as f:
    children = {}
    parents = {}
    for line in f:
        parent,child = list(line.strip().split(')'))
        if not parent in children:
            children[parent] = []
        children[parent].append(child)
        parents[child] = parent
    sum = 0
    for node in parents:
        while node in parents:
            node = parents[node]
            sum += 1
    print(sum)
    