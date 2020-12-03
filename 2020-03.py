#!/usr/bin/env python

import sys


filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'

print (f" using inputfile: {filename}")
with open(filename) as f:
    data = f.read().splitlines()

#print(f" read {len(data)} rows, data:\n{data}")

def solve1(forest, sx=3, sy=1):
    x = 0
    y = 0
    result = 0
    while y <  (len(forest) - 1 ):
        x, y = move(x, y, sx, sy, len(forest[0])-1)
        if forest[y][x] == '#':
            # print("Tree!")
            result += 1
    return(result)

def move(x, y, sx=3, sy=1, x_max=30):
    x += sx
    y += sy
    if x > x_max:
        x = x - x_max - 1
    return (x, y)

def solve2(forest):
    moves = ((1,1), (3,1), (5,1), (7,1), (1,2))
    result = 1
    for _ in moves:
        x = (solve1(forest, _[0], _[1]))
        result *= x
        # print (f" result/move: {x}/{_} = {result}")
    return result

print(f" solution1: {solve1(data)}")
print(f" solution2: {solve2(data)}")


