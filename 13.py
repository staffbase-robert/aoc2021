#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import re
import random

with open('13.input', 'r') as f:
    dots, splits = f.read().split('\n\n')
    dots = [[int(dd) for dd in d.split(',')] for d in dots.split('\n')]        
    splits = [re.match(r'fold along (\w)=(\d+)', split).groups() for split in splits.split('\n')[0:-1]]
    splits = [(split[0], int(split[1])) for split in splits]


    X = np.max([d[0] for d in dots]) + 1
    Y = np.max([d[1] for d in dots]) + 1

    pap = np.zeros((Y, X))

    for coord in dots:
        x, y = coord
        pap[y, x] = 1

    for s in splits:
        print(np.sum(pap))        
        if s[0] == 'x':
            fold = s[1]
            add = np.fliplr(pap[:, fold+1:pap.shape[1]])
            pap[:, fold - add.shape[1]:fold] += add
            pap = pap[:, 0:fold]

        if s[0] == 'y':
            fold = s[1]
            add = np.flipud(pap[fold+1:pap.shape[0]])
            pap[fold - add.shape[0]:fold] += add
            pap = pap[0:fold]
        pap = pap > 0
        pap = pap.astype(int)

    plt.imshow(pap)
    plt.show()
