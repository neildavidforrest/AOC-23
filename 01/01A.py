#!/usr/bin/env python3

def compute_value(input: str):
    return int([x for x in input if x.isdigit()][0] +
               [x for x in reversed(input) if x.isdigit()][0])

sum = 0
with open("input.txt") as f:
    line = f.readline()
    while line:
        sum += compute_value(line)
        line = f.readline()
print(sum)
