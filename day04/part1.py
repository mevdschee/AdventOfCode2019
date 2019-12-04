import os

dir = os.path.dirname(__file__)
with open(os.path.join(dir,"input")) as f:
    input = f.read().strip().split('-')
    count = 0
    for i in range(int(input[0]),int(input[1])):
        number = str(i)
        asc = True
        same = False
        for p in range(5):
            if number[p+1] < number[p]:
                asc = False
                break
            elif number[p+1] == number[p]:
                same = True
        if not asc or not same:
            continue
        count += 1
    print(count)