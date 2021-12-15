#!/usr/bin/env python3

import numpy as np
import re

with open('14.input', 'r') as f:
    start, rules = f.read().split('\n\n')
    
    rules_dict = {}
    rules = re.findall('(\w+)\s->\s(\w)', rules)
    for rule in rules:
        rules_dict[rule[0]] = rule[1]
    pol = start
    nxt = ""
    for i in range(10):
        for p in range(len(pol)-1):
            s = pol[p:p+2]
            ins = rules_dict[s]
            nxt += s[0] + ins
        nxt += pol[-1]
        pol = nxt
        nxt = ""
    
    freqs = {}
    for c in pol:
        if c in freqs:
            freqs[c] += 1
        else:
            freqs[c] = 1

    f = sorted(freqs.values())
    print(f[-1] - f[0])
    
