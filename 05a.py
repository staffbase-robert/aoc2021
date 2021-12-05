#!/usr/bin/env python3

import numpy as np
import re

def render(board, l):
    if l[0] == l[2]:
        a = l[1]
        b = l[3]
        if a > b:
            b, a = a, b

        board[a:b+1, l[0]] += 1
    elif l[1] == l[3]:
        a = l[0]
        b = l[2]
        if a > b:
            b, a = a, b

        board[l[1], a:b+1] += 1
    return board


with open('05.input', 'r') as f:
    lines = [[int(c) for c in g] for g in re.findall('(\d+),(\d+)\s->\s(\d+),(\d+)', f.read())]
    lines = list(filter(lambda l: l[0] == l[2] or l[1] == l[3], lines))
   
    m = np.max(np.array(lines)) + 1
    board = np.zeros((m,m))
    for line in lines:
        board = render(board, line)


    result = np.sum(board >= 2)
    print(result)
