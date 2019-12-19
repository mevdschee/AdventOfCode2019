import os

field = {}

dir = os.path.dirname(__file__)
with open(os.path.join(dir, "test1")) as f:
    lines = list(map(list,f.read().strip().split("\n")))
    width = len(lines[0])
    height = len(lines)
    