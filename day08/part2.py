import os

width, height = 25, 6
layers = []

dir = os.path.dirname(__file__)
with open(os.path.join(dir,"input")) as f:
    input = f.read().strip()
    for i in range(0, len(input), width*height):
        layers.append(input[i:i+width*height])
    final = list('2' * width*height)
    for layer in layers:
        for i in range(len(layer)):
            if final[i]=='2':
                final[i] = layer[i]
    for y in range(height):
        line = ''.join(final[y*width:(y+1)*width])
        print(line.replace('0',' ').replace('1','#'))