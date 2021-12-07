#!/usr/bin/env python3

import numpy as np

with open('07.input', 'r') as f:
    h = np.array([int(h) for h in f.read().split(',')])
    print(
        np.min(np.sum(np.array(([np.abs(h - mid) for mid in range(np.min(h), np.max(h)+1)])), axis=1))
    )

