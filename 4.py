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

    if n > 2:

        c += 1

    return c


x, n = map(int, input().split(" "))

s = list(input().split(" "))
b = []
q = []

for num in s:
    q.append(primeFactors(int(num)))
print("s")
