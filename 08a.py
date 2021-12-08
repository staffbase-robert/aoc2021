#!/usr/bin/env python3


#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg


segam = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8],
}

import numpy as np

def minus(a, b):
    uniq = a
    for bb in b:
        uniq = uniq.replace(bb, '')
    return uniq

def equal(a,b):
    return sorted(a) == sorted(b)

def find_nums(segs):
    nums = {}
    for seg in segs:
        if len(seg) == 2:
            nums[1] = seg

        if len(seg) == 4:
            nums[4] = seg

        if len(seg) == 3:
            nums[7] = seg

        if len(seg) == 7:
            nums[8] = seg

    ltormid = minus(nums[4], nums[1])
    top = minus(nums[7], nums[1])
    bot = None
    for seg in segs:
        if len(seg) != 5:
            continue
        res = minus(minus(seg, nums[4]), top)
        if len(res) == 1:
            bot = res

    for seg in segs:
        if equal(seg, nums[4] + top + bot):
            nums[9] = seg

    bl = minus(nums[8], nums[9])

    for seg in segs:
        if len(seg) != 5:
            continue
        res = minus(seg, nums[1] + bot + top)
        if len(res) == 1:
            nums[3] = seg
   
    zero_or_six = []
    for seg in segs:
        if len(seg) != 6 or seg == nums[9]:
            continue
        zero_or_six.append(seg)

    rem1 = minus(zero_or_six[0], zero_or_six[1])
    assert(len(rem1) == 1)

    rem2 = minus(zero_or_six[1], zero_or_six[0])
    assert(len(rem2) == 1)

    if rem1 in nums[1]:
        nums[0] = zero_or_six[0]
    elif rem2 in nums[1]:
        nums[0] = zero_or_six[1]

    mid = minus(nums[8], nums[0])
    lt = minus(ltormid, mid)

    for seg in segs:
        if len(seg) == 6 and seg != nums[0] and seg != nums[9]:
            nums[6] = seg


    for seg in segs:
        if len(seg) != 5 or seg == nums[3]:
            continue

        if lt in seg:
            nums[5] = seg
        else:
            nums[2] = seg

    return nums

with open('08.input', 'r') as f:
    res = 0
    for line in f.readlines():
        segs, code = line.split(' | ')
        segs = segs.split()
        

        nums = find_nums(segs)

        codes = np.array(code.split())
        
        for code in codes:
            for num in [nums[1], nums[4], nums[7], nums[8]]:
                if equal(code, num):
                    res += 1
        # print(np.isin(code, [nums[1], nums[4], nums[7], nums[8]]))
        # print(nums)
        # print(len(nums))
    print(res)
