#!/usr/bin/env python3

import numpy as np

def take_or_inf(arr, y, x):
    if x < 0:
        return 1e10
    if y < 0:
        return 1e10

    try:
        return arr[y, x]
    except IndexError as e:
        return 1e10


with open('09.input', 'r') as f:
    inp = np.array([[int(d) for d in l.strip()] for l in f.readlines()])
    s = inp.shape

    mask = np.empty_like(inp)
    print(range(s[0]), range(s[1]))
    for y in range(s[0]):
        for x in range(s[1]):
            left =      take_or_inf(inp, y, x-1)
            right =     take_or_inf(inp, y, x+1)
            top =       take_or_inf(inp, y-1, x)
            bottom =    take_or_inf(inp, y+1, x)
            middle =    inp[y, x]

            if middle < left and middle < right and middle < top and middle < bottom:
                mask[y, x] = 1
            else: 
                mask[y, x] = 0

    print(np.sum(inp * mask) + np.sum(mask))
