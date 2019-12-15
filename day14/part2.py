import os
import math

components = {}

dir = os.path.dirname(__file__)
with open(os.path.join(dir, "input")) as f:
    for line in f:
        pair = line.strip().split(' => ')
        target = pair[1].split(' ')
        chemical = target[1]
        quantity = int(target[0])
        sources = list(map(lambda i: i.split(' '), pair[0].split(', ')))
        components[chemical] = (quantity, [])
        for source in sources:
            components[chemical][1].append((source[1], int(source[0])))


def produce(chemical: str, quantity: int, unused: dict = {}) -> list:
    chemicals = {}
    if not chemical in components:
        return {chemical: quantity}
    quantity_per_unit, source_chemicals = components[chemical]
    if chemical in unused:
        quantity -= unused[chemical]
        del unused[chemical]
    no_of_units = math.ceil(quantity/quantity_per_unit)
    if no_of_units*quantity_per_unit > quantity:
        unused_quantity = no_of_units*quantity_per_unit - quantity
        unused[chemical] = unused.get(chemical, 0) + unused_quantity
    for source_chemical, source_quantity in source_chemicals:
        produce_quantity = no_of_units * source_quantity
        produced = produce(source_chemical, produce_quantity, unused)
        for chemical, quantity in produced.items():
            chemicals[chemical] = chemicals.get(chemical, 0) + quantity
    return chemicals


num = 0
val = 0
for start in range(64):
    val = produce('FUEL', 1 << start)['ORE']
    if val > 1000000000000:
        for pos in range(start-1, 0, -1):
            val = produce('FUEL', num | 1 << pos)['ORE']
            if val < 1000000000000:
                num |= 1 << pos
print(num)
