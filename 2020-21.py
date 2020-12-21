#!/usr/bin/env python

import sys
from collections import defaultdict


filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'
#filename += '_test'

print(f" using inputfile: {filename}")
d = []
tmp_list = []
with open(filename) as f:
    data = f.read().splitlines()

for x in data:
    ingred, allergens = x.split(' (')
    ingred = ingred.split(' ')
    allergens = allergens.rstrip(')').replace('contains ', '').replace(',', '').split(' ')
    d.append((ingred, allergens))

print(f"read {len(d)} dataset")
#print(f"first dataset: {d[0]}\nlast dataset: {d[-1]}")
print(f"all data: {d}\n")


def solve(data, solution2=False):
    dd = defaultdict(lambda: "")

    for x in data:
        for allergens in x[1]:
            if not dd[allergens]:
                 dd[allergens] = list(x[0])
            else:
                dd[allergens] = list( set(dd[allergens]).intersection(x[0]) )

    # flatten the list
    safe_ing = set([item for sublist in dd.values() for item in sublist])

    if not solution2:
        count = 0
        for x in data:
            for _ in x[0]:
                if _ not in safe_ing:
                    count += 1
        return count

    # solution2
    while solution2:
        solution2 = False
        for key in dd:
            if len(dd[key]) == 1:
                val = dd[key][0]
                for k in dd.keys():
                    if k == key:
                        continue
                    if val in dd[k]:
                       dd[k].remove(val)
                       solution2 = True

    solution2 = []
    for x in sorted(dd):
        solution2.append(dd[x])

    solution2 = ','.join([item for sublist in solution2 for item in sublist])
    return solution2



print(f"\n solution1: {solve(d)}\n")
print(f"\n solution2: {solve(d, solution2=True)}\n")


