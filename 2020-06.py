#!/usr/bin/env python

import sys
from collections import defaultdict

filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'

print(f" using inputfile: {filename}")
d = []
tmp_dict = {}
tmp_dict = defaultdict(lambda:0, tmp_dict)
groupcount = 0
with open(filename) as f:
    data = f.read().splitlines()
    for _ in data:
        if _ == '':
            d.append((tmp_dict, groupcount))
            groupcount = 0
            tmp_dict = {}
            tmp_dict = defaultdict(lambda: 0, tmp_dict)
            continue
        groupcount += 1
        for answer in _:
            tmp_dict[answer] = tmp_dict[answer] + 1
    d.append((tmp_dict, groupcount))


print(f"read {len(d)} dataset")
print(f"first dataset: {d[0]}\nlast dataset: {d[-1]}")


def solve1(data):
    result = 0
    for _ in data:
        result += len(_[0].keys())
    return result


def solve2(data):
    result = 0
    for _ in data:
        for key in _[0].keys():
            if _[0][key] >= _[1]:
                result += 1
    return result


print(f"\n solution1: {solve1(d)}")
print(f" solution2: {solve2(d) }")


