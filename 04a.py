#!/usr/bin/env python3

import numpy as np

with open('04.input', 'r') as f:
    a = f.read()
    a = a.split('\n\n')
    nums = [int(n) for n in a[0].split(',')]
    boards = a[1:]

    boards = [[[int(r) for r in rawnums.split()] for rawnums in board.split('\n') if rawnums] for board in boards]
    boards = np.array(boards)

    for i in range(len(nums)):
        c = np.isin(boards, nums[0:i+1])
        for b in range(c.shape[0]):
            # rows
            for row in range(c.shape[1]):
                arr = c[b, row]
                win = np.all(arr)
                if win:
                    print(np.sum(np.invert(c[b]) * boards[b]) * nums[i])
                    exit()

            # cols
            for col in range(c.shape[2]):
                arr = c[b, :, col]
                win = np.all(arr)
                if win:
                    print(np.sum(np.invert(c[b]) * boards[b]) * nums[i])
                    exit()
            # print(c[b])
        # print(c.shape)
        # print(c)
        # break
