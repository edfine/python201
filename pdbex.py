for num in range(1, 1000): # do something
    pass

print('do a lot more stuff')
x = int(input('Enter x: '))
if x == 1: # this is the buggy case
    print('and now we get to the bug...')
    import pdb
    pdb.set_trace() # causes the program to stop here, in the debugger
    print('buggy line')
else:
    y = x ** 2 # no debugging in this case
print(x)
