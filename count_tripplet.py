nr = input().rstrip().split()

n = int(nr[0])

r = int(nr[1])
di = {}
total = 0
arr = list(map(int, input().rstrip().split()))
arr.sort()
for x in arr:
    if x in di:
        di[x] += 1
    else:
        di[x] = 1
print(di)
for k, v in di.items():
    if (k*r in di and k*r*r in di):

        total = total+(v*di[k*r]*di[k*r*r])


print(total)
