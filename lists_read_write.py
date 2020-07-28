with open('1.txt') as f:
    word=f.readline()
    n=int(f.readline())
    c=[]
    for lines in f:
        c.append([int(x) for x in (lines.strip("\n").split(" ")) if x.isdigit() ])

print(c)
with open("2.txt","w") as r:
    for line in c:
        r.write(str(line)+'\n')

