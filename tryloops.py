n = int(input())

arr = list(map(int, input().rstrip().split()))

match=0
q=[p-1 for p in arr]
print(q)
for i,p in enumerate(q):
	if(i!=p):
		goto=q.index(i)
		temp=p
		q[i]=i
		q[goto]=temp
		match+=1
print(match)


