#!/usr/bin/env python

import sys
import re

filename = 'input_' + sys.argv[0].split('/')[-1].split('.')[0] + '.txt'

print(f" using inputfile: {filename}")
d = []
#
with open(filename) as f:
    data = f.read().splitlines()
    for _ in data:
        found = re.match(r'([FB]{7})([RL]{3})', _)
        if found:
            count = 1
            row = range(0, 127)
            while count <  (len(found[1]) + 1):
                if found[1][count-1] == 'F':
                    row = row[:int(len(row)/2)]
                else:
                    row = row[int(len(row)/2) + 1:]
                count += 1
            row = row.start

            count = 1
            column = range(0, 7)
            while count <  3:      # (len(found[2]) + 1):
                if found[2][count-1] == 'L':
                    column = column[:int(len(column)/2)]
                else:
                    column = column[int(len(column)/2) + 1:]
                count += 1
            if found[2][count-1] == 'R':
                column = column.stop
            else:
                column = column.start
            seat = row * 8 + column
            # print(f"row/column/seat: {row}/{column}/{seat}")

            d.append((found[0], row, column, seat))

print(f"read {len(d)} dataset")
print(f"first dataset: {d[0]}\nlast dataset: {d[-1]}\n\n")


def solve1(data):
    return max([n[3] for n in data])

def solve2(data):
   seats = sorted([n[3] for n in data])
   seat_max = max(sorted([n[3] for n in data]))
   seat_min = min(sorted([n[3] for n in data]))
   missing_seats = []
   for x in range(1, solve1(data)+1 ):
       if x < seat_min:
           continue
       if x > seat_max:
           continue
       if x not in seats:
           missing_seats.append(x)

   return (missing_seats[0])


print(f"\n solution1: {solve1(d)}")
print(f" solution2: {solve2(d)}")


