#!/usr/bin/env python3

import numpy as np

def cost(dist):
    dist = np.abs(dist)
    return dist * (dist + 1) / 2

with open('07.input', 'r') as f:
    h = np.array([int(h) for h in f.read().split(',')])
    print(
        np.min(np.sum(np.array(([cost((h - mid)) for mid in range(np.min(h),  np.max(h)+1)])), axis=1))
    )
