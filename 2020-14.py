#!/usr/bin/env python

import sys
import re
from collections import defaultdict

filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'
#filename += '_test'

print(f" using inputfile: {filename}")
d = []
tmp_list = []
with open(filename) as f:
    data = f.read().splitlines()
    for _ in data:
        if _ == '':
            continue
        else:
            if _.startswith('mask'):
                if tmp_list:
                    d.append((mask, tmp_list))
                    tmp_list = []
                mask = _.split('=')[1].strip()
            else:
                memory = re.match(r'^mem\[(\d+)\] = (\d+)$', _)
                tmp_list.append((int(memory[1]), int(memory[2])))
    d.append((mask, tmp_list))         # all input strings are int-numbers



print(f"read {len(d)} dataset")
print(f"first dataset: {d[0]}\nlast dataset: {d[-1]}")
print(f"all data: {d}\n")

def apply_mask(mask, value):
    one = int(mask.replace('X', '0'), 2)
    value |= one
    zero = int(mask.replace('X', '1'), 2)
    value &= zero
    return value

def solve1(data):
    memory = defaultdict(int)
    for n in data:
        mask = n[0]
        for addr, value in n[1]:
            memory[addr] = apply_mask(mask, value)
    result = 0
    print(memory)
    for val in memory.values():
        if val:
            result += val
    return result

def solve2(data):
    return


print(f"\n solution1: {solve1(d)}\n")






