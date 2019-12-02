import os

dir = os.path.dirname(__file__)
with open(os.path.join(dir,"input")) as f:
    sum = 0
    for line in f:
        sum+=int(line)//3-2
    print(sum)