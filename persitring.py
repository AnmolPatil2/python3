x = list(input("")[5:-1])
y = list(input("")[5:-1])
n = len(x)
co1 = 0
for i in range(len(y)):
    j = i
    co = 0

    while(j < len(y)):
        if(co == n):
            co1 += 1
        if(y[j] in x):
            j += 1
            co += 1

        else:
            break
print(co1)
