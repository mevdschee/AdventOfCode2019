import os

dir = os.path.dirname(__file__)
with open(os.path.join(dir,"input")) as f:
    parents = {}
    for line in f:
        parent,child = line.strip().split(')')
        parents[child] = parent
    sum = 0
    for node in parents:
        while node in parents:
            node = parents[node]
            sum += 1
    print(sum)
    