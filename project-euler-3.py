n = 600851475143

for i in range(2, int((n + 1) / 2)):

    while n % i == 0:

        print(n)
        n = n / i
