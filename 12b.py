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
    mem = {}
    for k in m:
        mem[k] = 0
    
    def has_visit_single_twice(mem):
        for memkey in mem:
            if memkey.islower() and mem[memkey] >= 2:
                return True
        return False

    def move(curr, trail, m, mem):
        for dest in m[curr]:
            if dest == 'start':
                continue
            if not dest.isupper() and mem[dest] > 0 and has_visit_single_twice(mem):
                continue
            else:
                if dest == 'end':
                    sol.append(trail + [curr, 'end'])
                else:
                    memcop = dict(mem)
                    memcop[dest] += 1
                    move(dest, trail + [curr], m, memcop)
    move('start', [], m, mem)

    print(len(sol))
