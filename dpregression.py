
def candies(start, arr, t):
    i = start
    print(arr[i])
    if(i+1 <= n):
        c = 0

        if(arr[i] >= arr[i+1]):
            while(arr[i] >= arr[i+1]):
                if(i+2 <= n):
                    c += 1
                    i += 1

                else:
                    print("i is {}".format(i))
                    if(arr[i] > arr[i+1]):
                        c += 1
                        for x in range(1, c+2):
                            t += x
                    else:
                        c += 1

                        for x in range(1, c+2):
                            t += x
                        t += 1

                    print(t)
                    exit(0)

            for x in range(1, c+2):
                t += x
            print("t here{}".format(t))
            i += 1
            candies(i,  arr, t)
        else:
            while(arr[i] < arr[i+1]):
                if(i+2 <= n):
                    i += 1

                    c += 1
                else:
                    if(arr[i] < arr[i+1]):
                        c += 1
                        for x in range(1, c+2):
                            t += x
                    else:
                        c += 1

                        for x in range(1, c+2):
                            t += x
                        t += 2
                    print(t)
                    exit(0)
            print("c{}".format(c))
            for x in range(1, c+2):
                t += x
            print("t {}".format(t))
            i += 1
            print("i {}".format(arr[i]))
            candies(i,  arr, t)
    else:
        t += 1
        print(t)
        exit


if __name__ == '__main__':

    n = int(input())
    n -= 1

    arr = []

    for _ in range(n+1):
        arr_item = int(input())
        arr.append(arr_item)

    candies(0,  arr, 0)
