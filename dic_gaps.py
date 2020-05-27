s = input()
s = list(s)
di = {}
for x in range(len(s)):
    di[x] = s[x]


def counter(x, y):
    print(di)


counter(0, len(s))
