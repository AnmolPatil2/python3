nm = input().split()

n = int(nm[0])

m = int(nm[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

l=[0 for i in range(0,n)]
for i in range(0,m):
	a,b,k=queries[i]
	a-=1
	b-=1
	z=[x+k for x in l[a:b+1]]
	
	l=l[0:a]+z+l[b+1:n]
	
