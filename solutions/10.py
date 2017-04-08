#!/usr/bin/env python3

'''
trying to create a datetime. see the documentation:
https://docs.python.org/3/library/datetime.html

that one was a bit mean... 'datetime' is a class in a module of the name
'datetime'. '.now()' can only be called on the class and not the module (as
the traceback kindly states).

we fix the import statement to

    from datetime import datetime

and we are good!
'''

from datetime import datetime

now = datetime.now()

print('it is: {}'.format(now))
