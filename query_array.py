import numpy as np

n,m=(int(x) for x in (input("").split()))
l=np.zeros(n,dtype=int)
for _ in range(m):
    a=[int(x) for x in (input("").split())]
    ta=a[0]
    l=a[1]
    r=a[2]
    if(ta==1):
        l[l-1:r]|=5
