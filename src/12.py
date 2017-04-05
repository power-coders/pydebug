#!/usr/bin/env python3

'''
fix!
'''


__cache = {}


def power2(x):
    """
    computes the power of 2 for a number x.

    Keeps results in memory because computing powers is expensive.
    """
    # if the result for x is not yet in memory, we compute it
    if __cache[x] is None:
        __cache[x] = 2 ** x

    return __cache[x]


power2(9)
power2(2)
power2(-4)
