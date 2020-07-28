def solutions(nums,target):
    h=len(nums)
    l=0
    while(l<h):
        mid=int((l+h)/2)
        if(nums[mid]==target):
            if(nums[mid+1]==target):
                return [mid,mid+1]
            else:
                return [mid-1,mid]
        elif(nums[mid]>target):
            h=mid-1
        else:
            l=mid+1
    return [-1,-1]
n=[int(x) for x in input("").split(",")]
t= int(input(""))
print(solutions(n,t))
