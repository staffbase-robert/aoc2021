#!/usr/bin/env python3

def loop(n, i, inv = False):
    bs = sum([(1 << i & nn) != 0 for nn in n]) >= len(n) / 2
    if inv:
        bs = not bs
    ret = []
    for nn in n:
        if ((1 << i & nn) != 0) == bs:
            ret.append(nn)
    return ret

with open('03.input', 'r') as f:
    m = 12 # change

    orig = [int(l, 2) for l in f.readlines()]
    n = orig

    for i in range(m-1, -1, -1):
        n = loop(n, i)
        if len(n) == 1:
            break
    
    ox1 = n

    n = orig
    for i in range(m-1, -1, -1):
        n = loop(n, i, True)
        if len(n) == 1:
            break
    
    ox2 = n

    print(ox1[0] * ox2[0])


        

