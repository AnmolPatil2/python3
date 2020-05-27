def solve():
    i = 1
    while(True):
        print(i)
        n = a*i

        if(n % x == 0):
            b1 = n//x
            n2 = b*i
            if(n2 % y == 0):
                b2 = n2//y
                print(str(b1)+" "+str(b2)+" "+str(i))
                break
        i += 1


x, y, a, b = [int(x) for x in input("").split()]
solve()
