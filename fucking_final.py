from math import sqrt


x, n = map(int, input().split(" "))

s = list(map(int, input().split(" ")))
b = []
q = []
m = max(s)


# Driver Code
N = m

arr = [0 for i in range(N + 5)]


for i in range(2, int((N)), 1):
    if(arr[i] > 0):
        continue
    else:
        for j in range(2 * i, N + 1, i):
            arr[j] += 1

    arr[i] = 1
i = 0
s = s[::-1]
v2 = []
while(i+x < n):
    m2 = 0

    for j in range(i, i+x):

        if(m2 < arr[s[j]]):
            m2 = arr[s[j]]
            jj = j
    v2.append(s[jj])
    i = jj+1

if(i < n):
    m2 = 0
    for j in range(n-1, n-x-1):

        if(m2 < arr[s[j]]):
            m2 = arr[s[j]]
            jj = j

    v2.append(s[jj])

print(min(v2))
