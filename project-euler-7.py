primes = []

n = 2
while True:

    isPrime = True

    for prime in primes:

        if n % prime == 0:

            isPrime = False
            break

    if isPrime:
        
        print(n)
        primes = primes + [n]

        if len(primes) == 10001:

            break
        
    n = n + 1
