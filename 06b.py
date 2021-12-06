#!/usr/bin/env python3

import numpy as np

with open('06.input', 'r') as f:
    m = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for f in f.readline().split(','):
        m[int(f)] += 1

    for i in range(256):
        m = {0: m[1], 1: m[2], 2: m[3], 3: m[4], 4: m[5], 5: m[6],  6: m[7] + m[0], 7: m[8], 8: m[0]}

    print(sum([m[k] for k in m]))
