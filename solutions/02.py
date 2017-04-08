#!/usr/bin/env python3

'''
dictionaries consist of key/value pairs: {key: value, ...}.

value addess is done this way: dct[key] (and not dct[0] for e.g. the first
element; dictionaries are unordered! the order in which you define the
dictionary or the order you see when you are printing it has *no* meaning!)

there are 3 ways to iterate over dictionaries:

    for key in dct:  # iterate over keys
        print(key)

this is identical to:

    for key in dct.keys():  # iterate over keys
        print(key)


then you can iterate over the values:

    for value in dct.values():  # iterate over values
        print(value)

and you can directly iterate over key/value pairs:

    for key, value in dct.items():  # iterate over key/value pairs
        print(key, value)

details here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries
'''

dct = {'a': 1, 'b': 2, 'c': 3}

print("the value of key 'b' is:", dct['b'])

# print out the numbers:
for value in dct.values():
    print(value)

# if you need them sorted, you have to state that:
for value in sorted(dct.values()):
    print(value)
