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
    bb = s[i:i+x]
    ww = max([arr[x] for x in bb)
