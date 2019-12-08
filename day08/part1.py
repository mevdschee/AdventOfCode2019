import os

width, height = 25, 6
layers = []

dir = os.path.dirname(__file__)
with open(os.path.join(dir,"input")) as f:
    input = f.read().strip()
    for i in range(0, len(input), width*height):
        layers.append(input[i:i+width*height])
    fewest_zeros = width * height
    result_ones = 0
    result_twos = 0
    for layer in layers:
        zeros = layer.count('0')
        ones = layer.count('1')
        twos = layer.count('2')
        if zeros<fewest_zeros:
            fewest_zeros=zeros
            result_ones = ones
            result_twos = twos
    print(result_ones*result_twos)