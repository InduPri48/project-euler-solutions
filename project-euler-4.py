def palindromic(n):

    f = str(n)

    return f == f[::-1]

n1 = 999
n2 = 999

p = []

for i in range(n1, 1, -1):

    for j in range(n2, 1, -1):

        n = i * j

        if palindromic(n):

            p = p + [n]

print(max(p))
