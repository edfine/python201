import random
import math
import os
from multiprocessing.pool import Pool

def prime_factor(value, level=0):
    factors = []
    if level:
        print('    ' * level, 'prime_factor(', value, ', ', level, ') ', os.getpid(), sep='')
        pass
    for divisor in range(2, value - 1):
        quotient, remainder = divmod(value, divisor)
        if not remainder:
            factors.extend(prime_factor(divisor, level + 1))
            factors.extend(prime_factor(quotient, level + 1))
            break
    else:
        factors = [value]
    return factors

if __name__ == '__main__': # distiguishes between running and importing
    pool = Pool()

    to_factor = [
        random.randint(40_000_000, 80_000_000) 
                for _ in range(64)
    ]
    print(to_factor)
    results = pool.map(prime_factor, to_factor)
    for value, factors in zip(to_factor, results):
        print("The factors of {} are {}".format(value, factors))
    #print(results)