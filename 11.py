#!/usr/bin/env python3

import numpy as np

def kernel(like, x, y):
    Y,X = like.shape
    ret = np.zeros((Y+2, X+2), dtype=int)
    kern = np.ones((3,3), dtype=int)
    ret[y:y+3, x:x+3]= kern
    ret = ret[1:Y+1, 1:X+1]
    assert(ret.shape == like.shape)
    return ret

def iter(curr, nxt, mem):
    Y,X = curr.shape
    for y in range(Y):
        for x in range(X):
            if mem[y, x] == 1:
                continue
            k = kernel(curr, x, y)
            look = (curr > 9)[y, x]
            nxt += k * look
            if look:
                mem[y,x] = 1
    return nxt
 
with open('11.input', 'r') as f:
    octs = [[int(a) for a in l.strip()] for l in f.readlines()]
    octs = np.array(octs)
    result = 0
    result_b = None
    i = 0
    while True:
        octs += 1
        mem = np.zeros_like(octs)
        while np.sum((octs > 9) * (1-mem)) > 0:
            nxt = octs
            octs = iter(octs, nxt, mem)
        octs *= 1 - mem
        result += np.sum(mem)
        if i == 99:
            print(result)
        if np.all(octs == 0):
            result_b = i
            break
        i+=1
     
    print(result_b+1)
