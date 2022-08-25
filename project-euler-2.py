lim = 4000000

n1 = 1
n2 = 2

s = 2
while True:

    n = n1 + n2

    if n > lim:
        break

    if n % 2 == 0:
        s = s + n
        
    n1 = n2
    n2 = n
    
print(s)
