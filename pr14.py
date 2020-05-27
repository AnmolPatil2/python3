
from itertools import combinations
arr=[]
count=0
def rSubset(arr, r): 
  
   return list(combinations(arr,r)) 
  
# Driver Function

for i in range(1,int(242280/4)):
	arr.append(i)
	
print(arr)
for a in (list(combinations(arr,3))  ):
	
	if (a[0]*a[0]+a[1]*a[1]==a[2]*a[2]):
		count=count+1
		print("count"+count)

