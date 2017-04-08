#!/usr/bin/env python3

'''
now we are using a mutable default argument on purpose: the cache is a
dictionary that will store already-calculated values for us.

the probmlem was

     if _cache[x] is None:

if there is no key 'x' in the '_cache' yet this will raise a 'KeyError'. just
replace that line with

    if x not in _cache:

will do just fine.



*BONUS*

note how python always claims that 'batteries are included'? this caching
(meomizing) feature is included in the python stantard library:
https://docs.python.org/3/library/functools.html#functools.lru_cache

see the second example (does exactly what our code does; only a lot nicer).
'''


import time
from functools import lru_cache


def long_running_f(x, _cache={}):
    """
    computes the power of 2 for a number x.

    Keeps results in memory because computing powers is expensive.
    """
    # if the result for x is not yet in memory, we compute it
    if x not in _cache:
        print('- calculating value for {}'.format(x))
        time.sleep(2)  # we preted this takes some time
        ret = 2 ** x
        _cache[x] = ret
    else:
        print('- can get value directly from cache for {}'.format(x))
        ret = _cache[x]

    return ret


@lru_cache()
def long_running_f2(x):
    """
    computes the power of 2 for a number x.

    Keeps results in memory because computing powers is expensive.
    """

    time.sleep(2)  # we preted this takes some time
    ret = 2 ** x

    return ret


for arg in (0, 1, -5, 3, 0, -3, 5, 3, 1, 2, 1, 4, 1, 4, -5, -3, 1, 5):

    ret = long_running_f(arg)
    print('long_running_f({:2d}) = {}'.format(arg, ret))

# check if that all works for our 2nd function:
for arg in (0, 1, -5, 3, 0, -3, 5, 3, 1, 2, 1, 4, 1, 4, -5, -3, 1, 5):

    ret = long_running_f2(arg)
    print('long_running_f2({:2d}) = {}'.format(arg, ret))

print(long_running_f2.cache_info())
