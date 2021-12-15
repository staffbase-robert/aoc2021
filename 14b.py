#!/usr/bin/env python3

import numpy as np
import re
import itertools
from tqdm import trange

with open('14.input', 'r') as f:
    start, rules = f.read().split('\n\n')
    
    rules_dict = {}
    rules = re.findall('(\w+)\s->\s(\w)', rules)
    for rule in rules:
        rules_dict[rule[0]] = rule[1]
    rules = rules_dict

    base = [v for v in rules.values()]
    base = list(set(base))
    perms = [''.join(r) for r in itertools.product(base, base)]
    edge_rules = {}
    for perm in perms:
        for p in range(len(perm)-1):
            s = perm[p:p+2]
            ins = rules[s]
            edge_rules[s] = (perm[p]+ins, ins+perm[p+1])
    # count edges in start
    edges_count = {}
    for p in range(len(start)-1):
        s = start[p:p+2]
        if s in edges_count:
            edges_count[s]+=1
        else:
            edges_count[s]=1
            
    for i in range(40):
        nxt_count = {}
        for edge in edges_count:
            count = edges_count[edge]
            pair = edge_rules[edge]
            for p in pair:
                if p in nxt_count:
                    nxt_count[p] += count
                else:
                    nxt_count[p] = count
        edges_count = nxt_count
        nxt_count = {}

    char_count = {}
    for edge in edges_count:
        for a in edge:
            if a in char_count:
                char_count[a] += edges_count[edge]
            else:
                char_count[a] = edges_count[edge]
    
    for char in char_count:
        char_count[char] //= 2

    sor = sorted(char_count.values())
    print(sor[-1] - sor[0] + 1)
