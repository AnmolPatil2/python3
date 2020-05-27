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

    if(N % 2 == 0):
        ec = N//2
        oc = N//2
    else:
        oc = int((N+1)/2)
        ec = int((N-1)/2)

    for ti in range(Q):
        cl = t[ti] % lc

        pos = M[ti]

        c = 0
        f = 0

        if(cl-oc <= 0):

            i = 0

            while(c < pos and i < oc):
                if(i < cl):
                    el = e[i]
                    c += 1
                    i += 1

                else:
                    el = o[i]

                    c += 1
                    if(c == pos):
                        print(o[i])
                        f = 1
                        break
                    else:
                        el = e[i]
                        c += 1

                    i += 1

            if(c == pos):
                if(f == 0):
                    print(el)
            else:
                print(-1)
        elif(cl-oc-ec <= 0):

            i = cl-oc

            if(i + pos-1 >= ec):

                print(-1)
            else:
                print(e[pos+i-1])
        elif(cl-oc-oc-ec <= 0):

            i = cl-int(N)-1

            if(i < pos-1):
                print(-1)
            else:
                print(o[pos-1])
        else:

            i = cl-int(N)-oc

            j = 0
            if(2*i >= pos):
                while(c < pos):
                    el = o[j]

                    c += 1

                    if(c == pos):
                        print(o[j])
                        f = 1
                        break
                    else:
                        el = e[j]
                        c += 1

                    j += 1

            else:

                i = pos-(i)-1
                if(i >= oc):
                    print(-1)
                    continue

                print(o[i])
                f = 1
                continue

            if(c == pos):
                if(f == 0):

                    print(el)
                else:

                    print(-1)


N = int(input())
A = list(map(int, input().split(" ")))


Q = int(input())
t = []
M = []
for i in range(Q):
    tmp = list(map(int, input().split(" ")))
    t.append(tmp[0])
    M.append(tmp[1])

DisappearanceOfIntegers(A, Q, M, t, N)
