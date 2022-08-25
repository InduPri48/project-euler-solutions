def isNatural(n):

    return n > 0 and n == int(n)

d = 1000

for a in range(1, 1000):

    b = (d ** 2 - 2 * a * d) / (2 *(d - a))

    if isNatural(a) and isNatural(b):

        c = d - a - b

        print(a, b, c, a * b * c)
