def DisappearanceOfIntegers(A, Q, M, t, N):
    e = []
    o = []
    for i in range(N):
        if(i % 2 == 0):
            e.append(A[i])
        else:
            o.append((A[i]))
    lc = N*2

    c = 0
    if(N % 2 == 0):
        ec = N//2
        oc = N//2
    else:
        oc = int((N+1)/2)
        ec = int((N-1)/2)
    erc = 0
    orc = 0
    for ti in range(Q):
        cl = t[ti] % lc
        pos = M[ti]
        tc = cl*100/lc
        if(tc <= 25.00):
            orc = cl
            i = 0
            while(c <= pos and i < N):
                if(i < cl):
                    el = e[i]
                    c += 1
                    i += 1
                else:
                    el = o[i]
                    c += 1
                    if(c == pos):
                        print(o[i])
                        break
                    else:
                        el = e[i]
                        c += 1
                    i += 1

            if(c == pos):
                print(el)
            else:
                print(-1)
        if(tc <= 50.00):

            i = cl-oc
            while(c <= pos-1 and i < N):
                el = e[i]
                c += 1
            if(c == pos):
                print(el)
            else:
                print(-1)
