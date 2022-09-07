primes = []

n = 2

while True:

    isPrime = True
    for prime in primes:

        if n % prime == 0:

            isPrime = False
            break

    if isPrime:

        if n < 2000000:

            primes = primes + [n]

        else:

            break

    n = n + 1

print(sum(primes))
