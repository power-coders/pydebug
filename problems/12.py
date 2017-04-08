#!/usr/bin/env python3

'''
now we are going to use the python feature we just learned about in the
previous example to cache values of a function.

suppose long_running_f is a function that runs for quite some time (we simulate
that here with time.sleep). assume this function is called many times but the
number of different arguments is small.

we do not want to repeat the long calculation (or data retrival/...). so we
store {argument: return_value} in a dictionary and just return the value if we
have calculated it already. otherwise we calculate the value, add it to the
cache and return it.

the code does not work as expected. please fix it!
'''


import time


def long_running_f(x, _cache={}):
    """
    computes the power of 2 for a number x.

    Keeps results in memory because computing powers is expensive.
    """
    # if the result for x is not yet in memory, we compute it
    if _cache[x] is None:
        print('- calculating value for {}'.format(x))
        time.sleep(2)  # we preted this takes some time
        ret = 2 ** x
        _cache[x] = ret
    else:
        print('- can get value directly from cache for {}'.format(x))
        ret = _cache[x]

    return ret


for arg in (0, 1, -5, 3, 0, -3, 5, 3, 1, 2, 1, 4, 1, 4, -5, -3, 1, 5):

    ret = long_running_f(arg)
    print('long_running_f({:2d}) = {}'.format(arg, ret))
