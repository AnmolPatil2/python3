t = int(input(""))
for s in range(t):
    n = int(input(""))
    if(n % 2 == 0):
        print(0)
    elif(n == 3):
        print(1)
    else:
        w = (n-3)/2

        print(int((2**w) % 1000000007))
