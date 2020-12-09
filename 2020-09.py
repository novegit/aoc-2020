#!/usr/bin/env python

import sys

filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'

print(f" using inputfile: {filename}")
d = []
with open(filename) as f:
    data = f.read().splitlines()
    for _ in data:
        if _ == '':
            continue
        else:
            d.append(int(_))         # all input strings are int-numbers
print(f"read {len(d)} dataset")
print(f"first dataset: {d[0]}\nlast dataset: {d[-1]}")
print(f"all data: {d}\n")


def slice_sums(data, position, preamble):
    start = position - preamble
    result = []

    for start in range(start,  position):
        loop = 1
        while start + loop < position:
            result.append(int(data[start]) + int(data[start+loop]))
            loop += 1
    return (list(set(result)))


def solve1(data, preambel=25):
    for x in range (preambel, len(data)):
        sums = slice_sums(data, x, preambel)
        if data[x] not in sums:
            return data[x]


def solve2(data, result_sum):
    d = [ x for x in data if x < result_sum]

    idx_d = 1
    for x in d:
        tmp_lst = [x]
        for _ in d[idx_d:]:
            tmp_lst.append(_)
            x = x + _
            if x == result_sum:
                return min(tmp_lst) + max(tmp_lst)
        idx_d += 1


print(f"\n solution1: {solve1(d, preambel=25)}")
print(f" solution2: {solve2(d, solve1(d, preambel=25)) }")