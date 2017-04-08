#!/usr/bin/env python3

'''
lst = list(range(10)) means:
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list elements are accessed by their index in the list.

    lst['10']

tries to access a list with a string. that will not work! and the index of the
last element is not 10 but 9 (indices start at 0).

in general you should access the last element of a list with

    lst[-1]

negative indices count from the end of the list.


search for 'slicing' here (or find an explanation for 'slice' in python).
https://docs.python.org/3/tutorial/introduction.html
'''

lst = list(range(10))

print('the last element is', lst[-1])

# loop through last 5 elements only (should print numbers 5, 6, 7, 8, 9)
for i in lst[5:]:  # ':'  was missing: we need a slice and not a single index.
    print(i)
