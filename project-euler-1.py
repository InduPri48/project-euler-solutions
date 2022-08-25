n = 1000

n_3 = int(n / 3)
n_5 = int(n / 5)

overlap = int(

if n % 3 == 0:
    n_3 = n_3 - 1

if n % 5 == 0:
    n_5 = n_5 + 1

s_3 = (3 * n_3 * (n_3 + 1)) / 2
s_5 = (5 * n_5 * (n_5 + 1)) / 2

s = s_3 + s_5

print(s)
