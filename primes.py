limit = 100
numbers = list(range(2, limit + 1))
primes = []

while numbers:
    candidate = numbers[0]
    primes.append(candidate)
    for num in range(candidate, limit + 1, candidate):
        if num in numbers:
            numbers.remove(num)

print(primes)

