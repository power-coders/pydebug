#!/usr/bin/env python3

'''
remove integers other than 5 from a list
'''

lst = list(range(10))

for n in lst:
    if n != 5:
        lst.remove(n)

# this should print a list containing only the number 5
print(lst)
