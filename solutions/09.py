#!/usr/bin/env python3

'''

    func = 'function'

assings 'func' to the str(ing) "'function'". then we try to call the string.
that will not work.

the fix is to remove the quotes:

    func = function

'''


def function(x=5):
    print('function({}) called!'.format(x))

func = function

func(9)
