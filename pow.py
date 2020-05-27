n = list(input(""))
t = 0
print(n)
for i in range(4):
    if(n[i] == "1"):
        t += 2**int(3-i)
print(t)
