#!/usr/bin/env python3

with open('01.input', 'r') as f:
    depths = [int(l) for l in f.readlines()]
    partial_sums = []

    for i in range(len(depths)-2):
        s = depths[i] + depths[i+1] + depths[i+2]
        partial_sums.append(s)

    print(sum([partial_sums[i] > partial_sums[i-1] for i in range(1, len(partial_sums))]))
