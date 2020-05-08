nd = input().split()

n = int(nd[0])


d = int(nd[1])

a = list(map(int, input().rstrip().split()))


s=n-d
print(s)
f=a[s:n]
print(f)
d=a[0:s]
f.extend(d)
print(f)