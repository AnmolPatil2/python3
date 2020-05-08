
a=[int(x) for x in list(input(""))]
to = 0
for i in range(0,4):
    
    to+=a[i]*(2**(3-i))
print(to)