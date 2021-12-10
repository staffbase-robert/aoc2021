#!/usr/bin/env python3

import numpy as np

def take_or_inf(arr, y, x):
    if x < 0:
        return float('inf')
    if y < 0:
        return float('inf')

    try:
        return arr[y, x]
    except IndexError as e:
        return float('inf')

def traverse(inp, y, x, out):
    out[y, x] = 1

    middle = inp[y, x]
    for pred in [
            lambda c: (c[0], c[1]-1),
            lambda c: (c[0], c[1]+1),
            lambda c: (c[0]-1, c[1]),
            lambda c: (c[0]+1, c[1])
        ]:
        c = pred((y, x))
        if c[0] < 0 or c[1] < 0:
            continue
        p = take_or_inf(inp, c[0], c[1])
        if p!= float('inf') and p > middle and p != 9:
            # print("compare {1} with {0}".format((c[0], c[1]), (y, x)))
            # pass
            traverse(inp, c[0], c[1], out)

with open('09.input', 'r') as f:
    inp = np.array([[int(d) for d in l.strip()] for l in f.readlines()])
    s = inp.shape
    mask = np.zeros_like(inp)
    basins = []
    for y in range(s[0]):
        for x in range(s[1]):
            left =      take_or_inf(inp, y, x-1)
            right =     take_or_inf(inp, y, x+1)
            top =       take_or_inf(inp, y-1, x)
            bottom =    take_or_inf(inp, y+1, x)
            middle =    inp[y, x]

            if middle < left and middle < right and middle < top and middle < bottom:
                basin = np.zeros_like(inp)
                traverse(inp, y, x, basin)
                basins.append(basin)



    print(np.sum(basins) + np.sum(inp == 9))
    result = [np.sum(b) for b in sorted(basins, key=lambda b: np.sum(b), reverse=True)[0:3]]
    print(np.prod(result))
        
