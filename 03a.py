#!/usr/bin/env python3

with open('03.input', 'r') as f:
    m = 12 # change

    n = [int(l, 2) for l in f.readlines()]

    gamma = 0
    eps = 0
    for i in range(m-1, -1, -1):
        bs = sum([(1 << i & nn) != 0 for nn in n]) > len(n) / 2
        gamma += bs * (1 << i)
        eps += (not bs) * (1 << i)
            
    print(gamma * eps)
