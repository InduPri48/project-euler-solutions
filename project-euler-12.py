def factors(n):

    f = []

    c = 2
    for i in range(2, int(n / 2) + 1):

        if n % i == 0:

            c = c + 1

    return c

n = 1
c = 2

n_divisors = 500
while True:

    l = factors(n)

    if l > n_divisors:

        print(n)

        break
    
    n = n + c

    c = c + 1
