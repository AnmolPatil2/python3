import math


def primeFactors(n):
    c = 0
    l = []

    while n % 2 == 0:

        if(2 not in l):
            l.append(2)
            c += 1
        n = n / 2

    for i in range(3, int(math.sqrt(n))+1, 2):

        while n % i == 0:

            if(i not in l):
                l.append(i)
                c += 1
            n = n / i

    if n > 2:

        if(n not in l):

            l.append(n)
            c += 1

    return c


def evaluate(a1, x, n):
    r = 0
    m = 0
    l = []
    v2 = []
    while(r < n-x+1):
        a2 = a1[r:x+r]
        print(a2)
        for i in range(len(a2)):
            if(a2[i] >= m):
                m = a2[i]
                ii = i
        l.append(r+ii)
        v2.append(m)

        r += 1
    print(l)
    print(v2)
    mm = v2[0]
    fi = l[0]

    for i in range(len(v2)):
        if(v2[i] < mm):
            mm = v2[i]
            fi = l[i]
    print(l)
    return fi


x, n = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
a1 = []
for i in a:
    a1.append(primeFactors(i))
print(a1)
out_ = evaluate(a1, x, n)
print(a[out_])
