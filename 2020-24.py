#!/usr/bin/env python

import sys
import re

filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'
#filename += '_test'

print(f" using inputfile: {filename}")
d = []
with open(filename) as f:
    data = f.read().splitlines()

for _ in data:
    d.append(re.findall(r'e|w|se|sw|ne|nw', _))


print(f"read {len(d)} dataset")
#print(f"first dataset: {d[0]}\nlast dataset: {d[-1]}")
print(f"all data: {d}\n")

def solve1(data):
    grid = set()
    for tile in data:
        x = 5
        y = 5
        for _ in tile:
            if _ == 'e':
                x += 1
            elif _ == 'w':
                x -= 1
            elif _ == 'se':
                x += 0.5
                y -= 1
            elif _ == 'sw':
                x -= 0.5
                y -= 1
            elif _  == 'ne':
                x += 0.5
                y += 1
            elif _ == 'nw':
                x -= 0.5
                y += 1

        if (x, y) in grid:
           grid.remove((x, y))
        else:
           grid.add((x, y))

    return len(grid)


print(f"\n solution1: {solve1(d)}\n")