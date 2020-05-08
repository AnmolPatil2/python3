import math


def primeFactors(n):
    c = 0
    l = []
    # Print the number of two's that divide n
    while n % 2 == 0:

        if(2 not in l):
            l.append(2)
            c += 1
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n))+1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:

            if(i not in l):
                l.append(i)
                c += 1
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:

        if(n not in l):

            l.append(n)
            c += 1

    return c


def evaluate(a, x, n):
    r = 0
    v1 = []
    c1 = []
    while(r < n-x+1):
        a1 = a[r:x+r]

        m = 1
        v = a[0]

        for i in reversed(a1):

            c = primeFactors(i)
            if(c > m):
                m = c
                v = i
        r += 1

        v1.append(v)
        c1.append(c)
        fc = 9999
        print(c1)
        print(v1)

    for i in range(len(c1)):
        if(c1[i] < fc):
            print(c1[i])
            fv = v1[i]
    return fv


x, n = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

out_ = evaluate(a, x, n)
print(out_)
