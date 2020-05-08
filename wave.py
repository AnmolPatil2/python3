s = input()
bal = 0
cnt = 0
m = 10000003
for i in s:
    if i == '(':
        bal += 1
    else:
        bal -= 1
    if m > bal:
        m = bal
        cnt = 0
    if m == bal:
        cnt += 1

if bal != 0:
    print(0)
else:
    print(cnt)
