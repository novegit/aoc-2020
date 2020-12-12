#!/usr/bin/env python

import sys
import re
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
            res = re.match(r'(\w)(\d+)$', _)
            d.append((res[1], int(res[2])))         # all input strings are int-numbers

print(f"read {len(d)} dataset")
#print(f"read {len(d[0])} dataset[0] length")
#print(f"first dataset: {d[0]}\nlast dataset: {d[-1]}")
#print(f"all data: {d}\n")


def move(cmd, pos):
    """
     cmd[0]: N E S W R L
     pos: { 'x': '', 'y': '', 'd': ''}
    """
    if cmd[0] == 'L':
        pos['d'] = pos['d'] - cmd[1]
        if pos['d'] < 0:
            pos['d'] = 360 + pos['d']
    elif cmd[0] == 'R':
        pos['d'] = pos['d'] + cmd[1]
        if pos['d'] >= 360:
            pos['d'] = pos['d'] - 360
    elif cmd[0] == 'N':
        pos['y'] = pos['y'] + cmd[1]
    elif cmd[0] == 'S':
        pos['y'] = pos['y'] - cmd[1]
    elif cmd[0] == 'E':
        pos['x'] = pos['x'] + cmd[1]
    elif cmd[0] == 'W':
        pos['x'] = pos['x'] - cmd[1]
    elif cmd[0] == 'F':
        if pos['d'] == 0:
            pos = move(("N", cmd[1]), pos)
        if pos['d'] == 90:
            pos = move(("E", cmd[1]), pos)
        if pos['d'] == 180:
            pos = move(("S", cmd[1]), pos)
        if pos['d'] == 270:
            pos = move(("W", cmd[1]), pos)
    return pos


def move2(cmd, pos, wppos):
    """
    """
    if cmd[0] == 'L':
        wppos['d'] = wppos['d'] - cmd[1]
        degree = cmd[1]
        if wppos['d'] < 0:
            wppos['d'] = 360 + wppos['d']
        if degree == 90:
            tmp = wppos['x']
            wppos['x'] = -1 * wppos['y']
            wppos['y'] = tmp
        if degree == 180:
            wppos['x'] = -1 * wppos['x']
            wppos['y'] = -1 * wppos['y']
        if degree == 270:
            tmp = wppos['x']
            wppos['x'] = wppos['y']
            wppos['y'] = -1 * tmp
    elif cmd[0] == 'R':
        wppos['d'] = wppos['d'] + cmd[1]
        degree = cmd[1]
        if wppos['d'] >= 360:
            wppos['d'] = wppos['d'] - 360
        if degree == 90:
            tmp = wppos['x']
            wppos['x'] = wppos['y']
            wppos['y'] = -1 * tmp
        if degree == 180:
            wppos['x'] = -1 * wppos['x']
            wppos['y'] = -1 * wppos['y']
        if degree == 270:
            tmp = wppos['x']
            wppos['x'] = -1 * wppos['y']
            wppos['y'] = tmp

    elif cmd[0] == 'N':
        wppos['y'] = wppos['y'] + cmd[1]
    elif cmd[0] == 'S':
        wppos['y'] = wppos['y'] - cmd[1]
    elif cmd[0] == 'E':
        wppos['x'] = wppos['x'] + cmd[1]
    elif cmd[0] == 'W':
        wppos['x'] = wppos['x'] - cmd[1]
    elif cmd[0] == 'F':
        n = cmd[1]
        pos['x'] = pos['x'] + wppos['x'] * n
        pos['y'] = pos['y'] + wppos['y'] * n

    return pos, wppos


def solve1(data):
    pos = { 'x': 0, 'y': 0, 'd': 90}

    for i in data:
        pos = move(i, pos)
    return abs(pos['x']) + abs(pos['y'])


def solve2(data):

    pos = { 'x': 0, 'y': 0, 'd': 90}
    wppos = { 'x': 10, 'y': 1, 'd': 90}

    for cmd in data:
        pos, wppos = move2(cmd, pos, wppos)
    return abs(pos['x']) + abs(pos['y'])


print(f"\n solution1: {solve1(d)}\n")
print(f" solution2: {solve2(d)}")






