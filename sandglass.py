arr = []
tsum=-9999
lsum=-9999
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
for i in range(1,5):
	for j in range(1,5):

		lsum=arr[i][j]+arr[i-1][j-1]+arr[i-1][j+1]+arr[i-1][j]+arr[i+1][j+1]+arr[i+1][j-1]+arr[i+1][j]
		if(tsum<lsum):
			tsum=lsum
print(tsum)
