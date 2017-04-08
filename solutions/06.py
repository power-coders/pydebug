#!/usr/bin/env python3

'''
take-home-message: *never* change a list (or anyghint you iterate over) while
you are looping over it (unless you *really* know what you are doing). this
will almost always end in tears!

filtering lists is most conveniently done using a list comprehension:
https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions

'''

lst = list(range(10))
lst = [value for value in lst if value == 5]

print(lst)
