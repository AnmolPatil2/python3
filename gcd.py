
def getDiff(A):
    if(A % 2 == 0):
        x = A/2
        y = x
    else:
        x = A//2
        y = x+1

    while(x > 0):
        a, b = x, y
        small = x

        for i in range(1, small+1):
            if((a % i == 0) and (b % i == 0)):
                gcd = i

        print(a)
        if(gcd == 1):
            print(y-x)
            break
        else:
            x -= 1
            y += 1


a = int(input(""))
getDiff(a)
