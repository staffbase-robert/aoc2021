#!/usr/bin/env python3

import numpy as np


with open('10.input', 'r') as f:
    o = '([{<'
    errors = {
        ')': 0,
        ']': 0,
        '}': 0,
        '>': 0
    }
    totals = []
    for l in f.readlines():
        trail = []
        no_good = False
        for b in l.strip('\n'):
            s = 0
            if b in o:
                trail.append(b)
            else:
                got = trail.pop()
                want = {
                    ')': '(',
                    ']': '[',
                    '}': '{',
                    '>': '<'
                }[b]
                if got != want:
                    errors[b] += 1
                    no_good = True
                    break
        if no_good:
            continue

        trail.reverse()
        completion = [
            {
            '(': ')',
            '[': ']',
            '{': '}',
            '<': '>'
        }[c]  for c in trail]
        c_score = 0
        for c in completion:
            c_score *= 5
            c_score += {
                ')': 1,
                ']': 2,
                '}': 3,
                '>': 4
            }[c]
        totals.append(c_score)



    result_a = errors[')'] * 3 + errors[']'] * 57 + errors['}'] * 1197 + errors['>'] * 25137
    result_b = sorted(totals)[len(totals)//2]
    
    print(result_a, result_b)
