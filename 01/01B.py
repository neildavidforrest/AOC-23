#!/usr/bin/env python3
from typing import Optional

names = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def to_digit(input: str, index: int) -> Optional[int]:
    if input[index].isdigit():
        return int(input[index])
    else:
        for name, number in names.items():
            if input[index:index+len(name)] == name:
                return number
    return None


def compute_value(input: str) -> int:
    first = None
    last = None
    for i in range(len(input)):
        if first is None:
            d = to_digit(input, i)
            if d is not None:
                first = d
        if last is None:
            d = to_digit(input, len(input) - 1 - i)
            if d is not None:
                last = d
    return int(f"{first}{last}")

sum = 0
with open("input.txt") as f:
    line = f.readline()
    while line:
        sum += compute_value(line)
        line = f.readline()
print(sum)
