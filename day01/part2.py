import os

dir = os.path.dirname(__file__)
with open(os.path.join(dir,"input")) as f:
    sum = 0
    for line in f:
        mass = int(line)
        while mass>0:
            mass=mass//3-2
            if mass>0:
                sum += mass
    print(sum)