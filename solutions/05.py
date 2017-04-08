#!/usr/bin/env python3

'''
'a' onlylives in the local namespace of 'f()' and is undefined in the global
namespace.
'''


def f():
    a = 5
    print(a)

f()
# print(a)  # just comment this out. 'a' is undefined here.
