#!/usr/bin/env python

import sys

filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'

print (f" using inputfile: {filename}")
d = [ ]
tmp_dict = {}

with open(filename) as f:
    data = f.read().splitlines()
    for _ in data:
        if _ == '':
            if tmp_dict.keys():
                d.append(tmp_dict)
            tmp_dict = {}
            continue
        tmp_list = []
        for tmp in _.split(' '):
            t0, t1 = tmp.split(':')
            tmp_list.append((t0, t1))
        tmp_dict.update(tmp_list)
d.append(tmp_dict)

print(f"read {len(d)} dataset")
print(f"first dataset: {d[0]}\nlast dataset: {d[-1]}")


def solve1(data):

    result = 0

    return(result)


def solve2(data):
    result = 0        # print (f" result/move: {x}/{_} = {result}")
    return result

print(f" solution1: {solve1(d)}")
print(f" solution2: {solve2(data)}")


