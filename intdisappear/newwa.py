import numpy as np


def DisappearanceOfIntegers(A, Q, M, t, N):
    e = []
    o = []
    for i in range(N):
        if(i % 2 != 0):
            e.append(A[i])
        else:
            o.append((A[i]))
    lc = N*2
    print(o)

    if(N % 2 == 0):
        ec = N//2
        oc = N//2
    else:
        oc = int((N+1)/2)
        ec = int((N-1)/2)

    for ti in range(Q):
        cl = t[ti] % lc

        pos = M[ti]
        tc = cl*100/lc

        c = 0
        if(tc <= 25.00):
            orc = cl
            i = 0
            f = 0

            while(c < pos and i < oc):
                if(i < cl):
                    el = e[i]
                    c += 1
                    i += 1
                    print("el"+str(el)+"i"+str(pos))
                else:
                    el = o[i]
                    print(el)
                    c += 1
                    if(c == pos):
                        print(o[i])
                        f = 1
                        break
                    else:
                        el = e[i]
                        c += 1
                        print(el)
                    i += 1

            if(c == pos):
                if(f == 0):
                    print(el)
            else:
                print(-1)
        elif(tc <= 50.00):

            i = cl-oc
            if(i+pos >= ec):

                print(-1)
            else:
                print(e[i+pos])
        elif(tc <= 75.00):
            i = cl-int(N)
            if(i < pos):
                print(-1)

            print(o[i])
        else:
            i = cl-int(N)-oc
            while(c < pos and i < ec):
                if(i > cl):
                    el = e[i]
                    c += 1
                    i += 1
                    print("el"+str(el)+"i"+str(pos))
                else:
                    el = o[i]
                    print(el)
                    c += 1
                    if(c == pos):
                        print(o[i])
                        f = 1
                        break
                    else:
                        el = e[i]
                        c += 1
                        print(el)
                    i += 1

                if(c == pos):
                    if(f == 0):
                        print(el)
                else:
                    print(-1)


N = int(input())
A = list(map(int, input().split(" ")))

print(A)
Q = int(input())
t = []
M = []
for i in range(Q):
    tmp = list(map(int, input().split(" ")))
    t.append(tmp[0])
    M.append(tmp[1])

DisappearanceOfIntegers(A, Q, M, t, N)
