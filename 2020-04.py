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


def solve1(data, solve2=False):
    result = 0
    cid = 0
    for _ in data:
        num_keys = len(_.keys())
        if num_keys == 7 and 'cid' not in _.keys():
            if solve2 and not validator(_):
                continue
            cid += 1
            continue
        if num_keys < 8:
            continue
        if solve2 and not validator(_):
            continue
        result += 1
    final = result + cid

    return final


def validator(d: dict):

    if not (d['byr'].isdigit() and 1920 <= int(d['byr']) <= 2002):
        return False
    if not (d['iyr'].isdigit() and 2010 <= int(d['iyr']) <= 2020):
        return False
    if not (d['eyr'].isdigit() and 2020 <= int(d['eyr']) <= 2030):
        return False

    if d['hgt'].endswith('cm'):
        _ = d['hgt'].replace('cm', '')
        if not (_.isdigit() and 150 <= int(_) <= 193):
            return False
    elif d['hgt'].endswith('in'):
        _ = d['hgt'].replace('in', '')
        if not (_.isdigit() and 59 <= int(_) <= 76):
            return False
    else:
        return False

    if not re.match(r"#[0-9a-f]{6}", d['hcl']):
        return False

    if d['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if len(d['pid']) != 9 or not d['pid'].isdigit():
        return False

    return True


print(f"\n solution1: {solve1(d)}")
print(f" solution2: {solve1(d, solve2=True)}")


