import math


def reddy(z):
    maxposition = 0
    m = z[0]
    for i in range(len(z)):
        if(z[i] >= m):
            m = z[i]
            maxposition = i

    return maxposition


def primeFactors(n):

    c = 0
    if (n % 2 == 0):

        c += 1
        while n % 2 == 0:

            n = n / 2
    i = 3
    while(i < int(math.sqrt(n))+1):
        if (n % i == 0):

            c += 1
        while n % i == 0:

            n = n / i
        i += 2

    if n > 2:

        c += 1

    return c


x, n = map(int, input().split(" "))

s = list(map(int, input().split(" ")))
b = []
q = []
for num in s:
        # print(num)
    q.append(primeFactors(num))
# print(s)
# print(q)
for i in range(n-x+1):
    r = reddy(q[i:i+x])

    b.append(s[i+r])
print(min(b))
