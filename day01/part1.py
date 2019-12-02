import os

dir = os.path.dirname(__file__)
sum = 0
with open(os.path.join(dir,"input")) as f:
    for line in f:
        sum+=int(line)//3-2
print(sum)