import math

# A function to print all prime factors of
# a given number n


def primeFactors(n):

    # Print the number of two's that divide n
    while n % 2 == 0:
        flist.append(2),
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n))+1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            flist.append(i),
            n = n / i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        flist.append(int(n))


t = int(input(""))
for e in range(t):
    n, m = [int(x) for x in (input("").split())]
    l = [int(x) for x in (input("").split())]
    flist = []
    re = []
    di = {}
    u = 65
    s = []
    (primeFactors(l[0]))
    for x in range(len(flist)):
        if(l[1] % flist[x] == 0):
            flist.append(int(l[1]/flist[x]))
            if x == 0:
                temp = flist[0]
                flist[0] = flist[1]
                flist[1] = temp

            break
    for x in range(2, len(l)):
        flist.append(int(l[x] / flist[-1]))
    s = flist.copy()
    flist = list(set(flist))
    flist.sort()

    for x in flist:

        di[x] = chr(u)
        u += 1
    o = []

    o = "".join(di.get(x) for x in s)
    print("Case #"+str(e+1)+": " + o)
