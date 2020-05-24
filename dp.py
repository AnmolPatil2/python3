
# Complete the maxSubsetSum function below.


def maxSubsetSum(arr):
    l1 = []
    l2 = []
    i = 0
    j = 0
    t1 = 0
    t2 = 0
    f = 0
    while(i < len(arr)):
        i += 2
        j += 3
        t1 += arr[i]
        t2 += arr[j]
        if(t1 > t2):
            if(f == 2):
                pass
            f = +1
        else:
            f = 0


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)
