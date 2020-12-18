#!/usr/bin/env python

import sys

filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'
#filename += '_test'

print(f" using inputfile: {filename}")
d = []
tmp_list = []
with open(filename) as f:
    data = f.read().splitlines()

d = [ _.replace('(', '( ').replace(')', ' )').split(' ') for _ in data ]

print(f"read {len(d)} dataset")
print(f"first dataset: {d[0]}\nlast dataset: {d[-1]}")
print(f"all data: {d}\n")

def solve_brackets(data, solution2=False):
    while data.count(')') != 0:
        c = 0
        for i in data:
            be = False
            if i == '(':
                bs = c
                c += 1
                continue
            if i == ')':
                be = c
                c += 1
                break
            c += 1
        # compute & replace
        if solution2:
            res = compute_slice2(data[bs + 1:be])
        else:
            res = compute_slice(data[bs + 1:be])
        data[bs:be+1] = [res]
    if solution2:
        res = compute_slice2(data)
    else:
        res = compute_slice(data)
    # print(f"line solution:{res}")
    return res

def compute_slice(data):
    last = int(data[0])
    for _ in range(1, len(data), 2):
        if data[_] == '+':
            last += int(data[_+1])
        elif data[_] == '*':
            last *= int(data[_ + 1])
    return last

def compute_slice2(data):
    while '+' in data and data.index('+'):
        idx = data.index('+')
        tmp = int(data[idx-1]) + int(data[idx+1])
        data[idx-1:idx+2] = [tmp]

    last = int(data[0])
    for _ in range(1, len(data), 2):
        if data[_] == '*':
            last *= int(data[_ + 1])
    return last

def solve1(data):
    result = 0
    for eq in data:
       result += solve_brackets(eq)
    return result

def solve2(data):
    result = 0
    for eq in data:
        result += solve_brackets(eq, solution2=True)
    return result

print(f"\n solution1: {solve1(d)}\n")
print(f"\n solution2: {solve2(d)}\n")


