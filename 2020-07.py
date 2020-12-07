#!/usr/bin/env python

import sys
import re

filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'

print(f" using inputfile: {filename}")
d = []
tmp_dict = {}

with open(filename) as f:
    data = f.read().splitlines()
    for _ in data:
        tmp1 = _.split('contain')
        key = tmp1[0].replace(' bags', '').strip()
        if key not in tmp_dict:
            tmp_dict[key] = {}
        tmp2 = tmp1[1].split(',')
        for tmp in tmp2:
            value = re.match('\s+(\d+) .*$', tmp)
            if value:
                tmp_bag = re.match('\s+\d+ (.*)$', tmp)
                tmp_bag = re.sub(r' bag(s)?.?', '',  tmp_bag[1])
                tmp_dict[key][tmp_bag] = value[1]
            else:
                tmp_dict[key][''] = 0


def solve1(data, key="shiny gold"):
    indirect = []

    for bag in data.keys():
        if key in data[bag]:
            indirect.append(bag)

    data_s = set(data.keys()) - set(indirect)
    tmp_indirect = indirect
    while True:
        data_s_old = len(data_s)
        indirect = tmp_indirect
        tmp_indirect = []
        for bag in data_s:
            for _ in data[bag].keys():
                if _ in indirect:
                    tmp_indirect.append(bag)
        data_s = data_s - set(tmp_indirect)
        if len(data_s) == data_s_old:
            break

    return len(data.keys()) - len(data_s)


def solve2(data, key="shiny gold"):

    return recursive_sum(data, key) - 1


def recursive_sum(bags, key):
    if key not in bags:
        return 0
    return 1 + sum(int(num) * recursive_sum(bags, key) for key, num in bags[key].items())


print(f"\n solution1: {solve1(tmp_dict)}")
print(f" solution2: {solve2(tmp_dict) }")