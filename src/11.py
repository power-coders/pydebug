#!/usr/bin/env python3

'''
this will show you a python feature that is important to be aware of.
i pretend to be ignorant of the feautre to show how it works.
can you fix it for me? i want the function to start with an empty list
every time it is called!
'''


def f(x, lst=[]):
    '''
    append x to lst.
    '''

    lst.append(x)
    return lst

print(f(0))
print(f('a'))
print(f([]))
