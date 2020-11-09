# This code lives in module.py
#
# Simple example of a Python module that exports functions
# to be used by other modules.
# 
# A possible use case is to package up a bunch of functions
# which are often used by your scripts.
#
# Inside your scripts you presumably have written
#
# import module
#
# or
#
# from module import func

def func(x):
    return x * 2

def dunder_main():
    return __name__

# What follows is a straightforward testing capability for this
# function (or functions). We notice that __name__ is set to
# __main__ when we *run* this script, but it's set to the name
# of this module when we import this module.

if __name__ == '__main__':
    # We ran this script, rather than importing it
    print('Running unit tests...')
    assert func(2) == 4
    assert func('two') == 'twotwo'
    print('All tests passed!')