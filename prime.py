
def solve(A):
    l = []

    def divs(x):
        for j in range(1, x+1):
            if(x % j == 0):
                l.append(j)
    for i in A:

        divs(int(i))
    n = sum(l)
    p = [1]
    print(n)
    for i in range(2, n):

        if(i > 1):
            for j in range(2, i-1):

                if(i % j == 0):
                    break
            else:
                p.append(i)
    tt = []
    print(p)
    for i in range(len(p)-1, len(p)-4, -1):
        a = n
        a = a-p[i]

        while(a > 0):

            c = 1
            for j in range(len(p)):

                if(p[j] > a):
                    c += 1
                    j = j-1
                    a = a-p[j]
                    if(a == 0):
                        tt.append(c)
                    break
        print(tt)


a = list(input("").split(" "))
solve(a)
