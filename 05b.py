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
    else:
        p1 = (l[0], l[1])
        p2 = (l[2], l[3])

        if p1[0] > p2[0]:
            p1, p2 = p2, p1

        up = p1[1] > p2[1]
        i = 0
        for x in range(p1[0], p2[0]+1):
            board[p1[1]+ (-i if up else i), x] += 1 
            i+=1
     
    return board


with open('05.input', 'r') as f:
    lines = [[int(c) for c in g] for g in re.findall('(\d+),(\d+)\s->\s(\d+),(\d+)', f.read())]
    m = np.max(np.array(lines)) + 1
    board = np.zeros((m,m))
    for line in lines:
        board = render(board, line)
    result = np.sum(board >= 2)
    print(result)
