#!/usr/bin/env python3

import numpy as np
import re

with open('12.input', 'r') as f:
    segs = re.findall('(\w+)-(\w+)', f.read())
    m = {}

    for seg in segs:
        a, b = seg
        if a in m:
            m[a].append(b)
        else:
            m[a] = [b]
        
        if b in m:
            m[b].append(a)
        else:
            m[b] = [a]

    sol = []    
    def move(curr, trail, m):
        for dest in m[curr]:
            if dest in trail and not dest.isupper():
                continue
            else:
                if dest == 'end':
                    sol.append(trail + [curr, 'end'])
                else:
                    move(dest, trail + [curr], m)
    move('start', [], m)
    print(len(sol))
