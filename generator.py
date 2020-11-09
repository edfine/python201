
def is_prime(num):
    import math
    if num > 2 and num % 2 == 0:
       return False
    for pd in range(3, int(math.sqrt(num)) + 1, 2):
        if num % pd == 0:
            return False
    return True

def get_primes(num):
    while True:
        if is_prime(num):
            print("get_primes yielding", num)
            num = yield num 
            print("get_primes received", num)
        num += 1

def print_successive_primes(iterations, base=10):
      prime_generator = get_primes(base)
      prime_generator.send(None)
      for power in range(iterations):
          print(prime_generator.send(base ** power))

print_successive_primes(6)
