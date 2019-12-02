import os

dir = os.path.dirname(__file__)
sum = 0
with open(os.path.join(dir,"input")) as f:
    for line in f:
        mass = int(line)
        while mass>0:
            mass=mass//3-2
            if mass>0:
                sum += mass
print(sum)