import numpy as np


def DisappearanceOfIntegers(A, Q, M, t, N):
    def final(x, y):

        l = arr[x]

        c = 0
        i = 0
        while(c <= y-1 and i < N+1):
            p = l[i]*A[i]
            if(p != 0):
                c += 1
            i += 1

        if(c == y):
            print(p)
        else:
            print(-1)

    if(N % 2 == 0):
        ec = N//2
        oc = N//2
    else:
        oc = int((N+1)/2)
        ec = int((N-1)/2)

    lc = N*2
    l = [1 for x in range(N+1)]

    j = 1

    i = 1
    arr = np.array(l)
    while(i <= oc):

        l[j] = 0
        j += 2
        i += 1
        x = np.array(l)
        arr = np.vstack([arr, x])

    j = 2
    i = 1

    while(i <= ec):
        l[j] = 0
        j += 2
        i += 1
        x = np.array(l)
        arr = np.vstack([arr, x])

    j = 1
    i = 1
    while(i <= oc):
        l[j] = 1
        j += 2
        i += 1
        x = np.array(l)
        arr = np.vstack([arr, x])
    j = 2
    i = 1
    while(i <= ec):
        l[j] = 1
        j += 2
        i += 1
        x = np.array(l)
        arr = np.vstack([arr, x])

    for ti in range(Q):
        cl = t[ti] % lc
        pos = M[ti]

        final(cl, pos)


N = int(input())
A = list(map(int, input().split(" ")))
A.insert(0, 0)
A = np.array(A)

Q = int(input())
t = []
M = []
for i in range(Q):
    tmp = list(map(int, input().split(" ")))
    t.append(tmp[0])
    M.append(tmp[1])

DisappearanceOfIntegers(A, Q, M, t, N)
