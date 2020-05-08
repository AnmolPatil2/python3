n, m, j = [int(x) for x in input("").split()]
n = n-1
m = m-1
times = (n % j)+1
times1 = (m % j)+1
box = (n//j)+1
box1 = (m//j)+1
out = (times*box)*(times1*box1)
print(out)
