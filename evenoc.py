n = int(input(""))
l = sorted([int(x) for x in input("").split()])

t = 0
i = 0
c = 1
j = 1
while(j < n):

    if(l[i] == l[j]):
        c = (c+1) % 2

        j += 1
    else:

        if(c == 0):
            t += l[i]

        i = j
        j = i+1
        c = 1
if(c == 0):
    t += l[i]
print(t)
