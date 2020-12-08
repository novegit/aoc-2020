#!/usr/bin/env python

import sys
from collections import defaultdict

filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'

print(f" using inputfile: {filename}")
d = []
groupcount = 0
with open(filename) as f:
    data = f.read().splitlines()
    for _ in data:
        if _ == '':
            continue
        else:
            order, arg = _.split(' ')
            d.append([order, arg])
print(f"read {len(d)} dataset")
print(f"first dataset: {d[0]}\nlast dataset: {d[-1]}")


def exec_code(data, position, accumulator):
    if data[position][0] == 'nop':
        return (position + 1, accumulator)
    if data[position][0] == 'acc':
        return (position + 1, accumulator + int(data[position][1]))
    if data[position][0] == 'jmp':
        return (position + int(data[position][1]), accumulator)


def solve1(data):
    exec_dict = {}
    exec_dict = defaultdict(lambda: 0, exec_dict)
    exec_position = 0
    accumulator = 0
    while True:
        exec_dict[exec_position] += 1
        exec_position_last = exec_position
        accumulator_last = accumulator
        exec_position, accumulator = exec_code(data, exec_position, accumulator)
        if exec_dict[exec_position_last] > 1:
            return (accumulator_last, False)
        if exec_position == len(data):
            return (accumulator, True)


def solve2(data):
    result = 0
    for cmd in ['nop', 'jmp']:
        count = 0
        for _ in data:
            if data[count][0] == cmd:
                data[count][0] = switch(cmd)
                solve_result = solve1(data)
                if not solve_result[1]:
                    data[count][0] = cmd
                else:
                    return solve_result[0]
            count += 1
    return result


def switch(cmd):
    return 'nop' if cmd == 'jmp' else 'jmp'


print(f"\n solution1: {solve1(d)[0]}")
print(f" solution2: {solve2(d) }")