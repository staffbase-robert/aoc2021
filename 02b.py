#!/usr/bin/env python3
import numpy as np


with open('02.input', 'r') as f:
    raw = [l for l in f.readlines()]
    pos = np.array([0,0])
    aim = 0
    for r in raw:
        d, a = r.split(" ")
        a = int(a)
        if d == 'forward':
            pos[0] += a
            pos[1] += aim * a
        if d == 'up':
            aim -= a
        if d == 'down':
            aim += a

    print(pos[0] * pos[1])
