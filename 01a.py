#!/usr/bin/env python3

with open('01.input', 'r') as f:
    depths = [int(l) for l in f.readlines()]
    print(sum([depths[i] > depths[i-1] for i in range(1, len(depths))]))
