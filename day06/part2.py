import os

dir = os.path.dirname(__file__)
with open(os.path.join(dir,"input")) as f:
    parents = {}
    for line in f:
        parent,child = list(line.strip().split(')'))
        parents[child] = parent
    sum = 0
    paths = [["YOU"],["SAN"]]
    for path in paths:
        while path[-1] in parents:
            path.append(parents[path[-1]])
    for p0 in range(len(paths[0])):
        node = paths[0][p0]
        if node in paths[1]:
            p1 = paths[1].index(node)
            print(p0+p1-2)
            exit()
