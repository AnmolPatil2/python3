mn=input("").split()
m=mn[0]
n=mn[1]
l=[]
for i in range(n):
    l.append([int(x) for x in (input("").split(""))])
for i in range(n):
    for j in range(m):
        