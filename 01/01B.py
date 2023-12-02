#!/usr/bin/env python3

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


def to_digits(input: str):
    min_idx = int(float("inf"))
    min_value = ""
    min_key = ""
    max_idx = int(float("-inf"))
    max_value = ""
    max_key = ""
    for key, value in names.items():
        idx = input.find(key)
        if idx != -1 and idx < min_idx:
            min_idx = idx
            min_value = value
            min_key = key
        idx = input.rfind(key)
        if idx != -1 and idx > max_idx:
            max_idx = idx
            max_value = value
            max_key = key

    overlap = 0
    if max_idx >= 0 and max_idx != min_idx:
        if max_idx < min_idx + len(min_key):
            overlap = min_idx + len(min_key) - max_idx
        input = input[0:max_idx] + str(max_value) + input[max_idx + len(max_key) :]
    if min_idx >= 0:
        input = (
            input[0:min_idx]
            + str(min_value)
            + input[min_idx + len(min_key) - overlap :]
        )
    return input


def compute_value(input: str):
    return int(
        [x for x in input if x.isdigit()][0]
        + [x for x in reversed(input) if x.isdigit()][0]
    )


sum = 0
with open("input.txt") as f:
    line = f.readline()
    while line:
        sum += compute_value(to_digits(line))
        line = f.readline()
print(sum)
