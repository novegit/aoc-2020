#!/usr/bin/env python

import sys
from collections import defaultdict
from functools import lru_cache

filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'
#filename += '_test'

print(f" using inputfile: {filename}")
d = []
with open(filename) as f:
    data = f.read().splitlines()
    for _ in data:
        if _ == '':
            continue
        else:
            d.append(int(_))         # all input strings are int-numbers
d = sorted(d)
print(f"read {len(d)} dataset")
print(f"first dataset: {d[0]}\nlast dataset: {d[-1]}")
print(f"all data: {d}\n")


def solve1(data):
    diff_dict = {}
    diff_dict = defaultdict(lambda: 0, diff_dict)
    diff_dict[min(d)] += 1
    diff_dict[3] += 1
    solv_list = [d[0]]
    x = 0
    for y in range(1,len(d)):
        di = data[y] - data[x]
        if di <= 3:
            diff_dict[di] += 1
            solv_list.append(d[y])
            x += 1
        continue
    return (diff_dict[1] * diff_dict[3], solv_list)

@lru_cache(maxsize=None)
def solve(data, prev, i):
    if i == len(data): return 1
    if data[i] - prev > 3: return 0
    x = solve(data, data[i], i+1)
    if i+1 < len(data) and data[i+1] - prev <= 3:
        x += solve(data, prev, i+1)
    return x

def solve2(data):
    return solve(tuple(data), 0, 0)

print(f"\n solution1: {solve1(d)[0]}\n")

print(f" solution2: {solve2(d)}")






