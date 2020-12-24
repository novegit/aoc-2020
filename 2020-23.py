#!/usr/bin/env python

import sys
from collections import deque, defaultdict
import time
from copy import deepcopy

filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'
#filename += '_test'

print(f" using inputfile: {filename}")
d = []
with open(filename) as f:
    data = f.read().splitlines()

d = [int(x) for x in data[0]]

print(f"read {len(d)} dataset")
#print(f"first dataset: {d[0]}\nlast dataset: {d[-1]}")
print(f"all data: {d}\n")

class Ring:
    def __init__(self, l):
        if not len(l):
            raise "ring must have at least one element"
        self._data = l
    def __repr__(self):
        return repr(self._data)
    def list(self):
        return self._data
    def len(self):
        return len(self._data)
    def get(self, i, up=False):
        if not up:
            return self._data[i]
        return self._data[i:up]
    def set(self, low, up, values):
        if not up:
            self._data[low] = values
        self._data[low:up] = values
    def index(self, value):
        return self._data.index(value)
    def turn(self):
        last = self._data.pop(-1)
        self._data.insert(0, last)
    def forward(self):
        last = self._data.pop(0)
        self._data.insert(len(self._data), last)
    def first(self):
        return self._data[0]
    def last(self):
        return self._data[-1]


def solve1(data):
    d = Ring(data)
    print(d)
    count = 0
    while count < 100:
        count += 1
        print(f"c {count} - d:{d.list()}")
        part = d.get(1,4)
        # list without the 3 pickups
        tmp_d = d.list()
        for x in part:
            tmp_d.remove(x)

        dest = d.first() - 1
        if dest < min(d.list()):
            dest = max(d.list())
        while dest in part:
            dest -= 1
            if dest < min(d.list()):
                dest = max(d.list())
        idx = d.index(dest)
        d.set(idx+1, idx+1, part)
        d.forward()

    while d.list()[0] != 1:
        d.forward()
    return ''.join(map(str, d.list()[1:]))



def solve2(data):
    return

print(f"\n solution1: {solve1(d)}\n")
print(f"\n solution2: {solve2(d)}\n")
