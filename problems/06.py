#!/usr/bin/env python3

'''
we want to remove all integers other than 5 from a list.

run the code, be amazed and try to come up with a solution.

don't hurt yourself too much if you can't make this one work. go have a look
at the solution once you have exhausted all your ideas.
'''

lst = list(range(10))

for n in lst:
    if n != 5:
        lst.remove(n)

# this should print a list containing only the number 5
print(lst)
