#!/usr/bin/env python3

'''
the function is never called. 'function' is just a reference to the function
object of the function. that is valid python - the statement just does not
do anything.

in order to call the function, you must add '()': function().
'''


def function():
    print('function called!')

function()  # added '()' to *call* the function.
