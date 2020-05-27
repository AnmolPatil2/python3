def maxLeftSubArraySum(a, size, sum):
    max_so_far = a[0]
    curr_max = a[0]
    sum[0] = max_so_far
    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        sum[i] = curr_max
        print(sum)
        
 
def maxRightSubArraySum(a, n, sum): 
 
	max_so_far = a[n] 
	curr_max = a[n] 
	sum[n] = max_so_far 
 
	for i in range(n - 1, -1, -1): 
	
		curr_max = max(a[i], curr_max + a[i]) 
		sum[i]=curr_max
 
 
def findMaxAbsDiff(arr, n): 
 
 
	leftMax = [0 for i in range(n+1)] 
	maxLeftSubArraySum(arr, n, leftMax) 
 
	rightMax = [0 for i in range(n+1)] 
	maxRightSubArraySum(arr, n-1, rightMax) 
 
	invertArr = [0 for i in range(n)] 
	for i in range(n): 
		invertArr[i] = -arr[i] 
 
	leftMin = [0 for i in range(n+1)] 
	maxLeftSubArraySum(invertArr, n, leftMin) 
	for i in range(n): 
		leftMin[i] = -leftMin[i] 
 
	rightMin = [0 for i in range(n+1)] 
	maxRightSubArraySum(invertArr, n - 1, rightMin) 
	for i in range(n): 
		rightMin[i] = -rightMin[i] 
 
	result = -2147483648
	for i in range(n): 
 
		absValue = max(abs(leftMax[i] - rightMin[i + 1]), 
					abs(leftMin[i] - rightMax[i + 1])) 
		if (absValue > result): 
			result = absValue 
	
	return result 
	
n=int(input())
a=list(map(int,input().split(' ')))
print(findMaxAbsDiff(a, n)) 
 
