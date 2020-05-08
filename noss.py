# Write your code here
n = [int(x) for x in (list(input("")))]
q = int(input(""))
for i in range(q):
    l = [int(x) for x in (input("").split(" "))]
    if(l[0] == 2):
        x = n[l[1]-1:l[2]]
        print(x)
        x.sort(reverse=True)
        print(x)
        print(x[l[3]-1])
    else:
        n[l[1]-1] = l[2]
