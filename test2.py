#!/bin/python3

import sys


def solve(n):
    if (n < 1 or n >= 1000000000):
        return 0
        exit()

    sum = 0
    for i in range(n):
        if (i % 3 == 0 or i % 5 == 0):
            sum += i
    return sum


t = int(input().strip())
if (t < 1 or t >= 100000):
    print(0)
    exit()
for a0 in range(t):
    n = int(input().strip())
    result = solve(n)
    print(result)
