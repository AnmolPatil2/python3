def solve(A, B):
    x = list(A)
    y = list(B)
    n = len(x)
    co1 = 0
    for i in range(len(y)):
        r = x.copy()
        co = 0
        j = i

        while(j < len(y)):
            print(r)
            print(y[j])

            if(y[j] in r):
                r.remove(y[j])
                print(r)
                j += 1
            if(len(r) == 0):
                co1 += 1
                print(r)
                break
            else:
                break

    return (co1)


x = (input(""))
y = (input(""))
print(solve(x, y))
