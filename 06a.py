#!/usr/bin/env python3

import numpy as np

class Fish():
    def __init__(self, t):
        self.t = int(t)

    def __repr__(self):
        return "f{0}".format(self.t)


    def __str__(self):
        return "f{0}".format(self.t)

    def next(self):
        self.t -= 1
        if self.t < 0:
            self.t = 6
            return Fish(8)
            
        return 

with open('06.input', 'r') as f:
    fishs = [Fish(f) for f in f.readline().split(',')]

    new_fish = []
    for i in range(80):
        for f in fishs:
            n = f.next()
            if n is not None:
                new_fish.append(n)
        fishs.extend(new_fish)
        new_fish = []

    print(len(fishs) + len(new_fish))

