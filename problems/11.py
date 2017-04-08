#!/usr/bin/env python3

'''
this will show you a python feature that is important to be aware of. we
pretend to be ignorant of the feautre to show how it works. can you fix it for
us?

the function f is supposed to get one argument and return the argument as
only item in a list. (of course we could just have returned '[x]' or 'list(x)'
but we want to use append for this one).

look at what is happening... can you fix that without changing the last 2 lines
of f?
'''


def f(x, lst=[]):
    '''
    append x to lst.
    '''

    lst.append(x)  # do not modify this line
    return lst     # do not modify this line

print(f(0))    # expecting [0]
print(f('a'))  # expecting ['a']
print(f([]))   # expecting [[]]
