primes = []

n = 2
for i in range(2000000):

    isPrime = True
    for prime in primes:

        if i % prime == 0:

            isPrime = False
            break

    if isPrime:

        primes = primes + [n]

    n = n + 1

print(sum(primes))
