#!/usr/bin/env python3

'''
take-home-messsage: do not use mutable arguments (lists, dictionaries, ...)
as arguments in functions (unless you do it on purpose). immutable arguments
(None, int, float, str, tuple, ...) will not lead to surprises.

the pattern you will see a lot is to use None as default argument (None is
immutable) and then check for that in the function body:
'''


def f(x, lst=None):  # use None as default argument for mutable lst
    '''
    append x to lst.
    '''

    if lst is None:  # now check for None
        lst = []     # and assign to []
    # lst = lst if lst is not None else []  # or do that in one line

    lst.append(x)  # do not modify this line
    return lst     # do not modify this line

print(f(0))    # expecting [0]
print(f('a'))  # expecting ['a']
print(f([]))   # expecting [[]]
