#!/usr/bin/env python3

'''
the solution.

there was 1 space too many on the first print line.
you also could have added a space before 'if' and 'else': this would have
resulted in correct python code as well. but it is considered bad style to have
indentations that are not multiples of 4 spaces.
see: https://www.python.org/dev/peps/pep-0008/

then there were the ':' missing for the 'if/else' statement.
'''

for i in range(10):
    print(i)        # indentation was off here: 1 space too many
    if i % 2 == 0:  # ':' was missing here
        print('even!')
    else:           # ':' was missing here
        print('odd')
