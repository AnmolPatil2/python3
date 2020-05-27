from itertools import permutations
t = int(input(""))


for z in range(t):
    k, n, p = [int(x) for x in (input("").split())]
    d = []
    for _ in range(k):
        l1 = [int(x) for x in (input("").split())]
        for i in range(1, n):
            l1[i] = l1[i]+l1[i-1]

        d.append(l1)


################################################################
    gs = 0
    sus = []

    def solve(l):

        o1 = 0
        no_of_z = k2-len(l)
        for i in range(no_of_z):
            l.append(0)

        perm = permutations(l)

        for i in (perm):

            locs = 0
            for j in range(len((i))):

                if(i[j] != 0):

                    locs += d[o1][i[j]-1]
                o1 = o1+1
            o1 = 0

            if(locs > gs):
                sus.append(locs)

    def findCombinationsUtil(arr, index, num,
                             reducedNum):

        # Base condition
        if (reducedNum < 0):
            return

        # If combination is
        # found, print it
        if (reducedNum == 0):
            if(index <= k2):

                for i in range(index):
                    if(arr[i] > n2):
                        i = i-1
                        break
                nl = []
                if(i == index-1):
                    for i in range(index):
                        nl.append(arr[i])
                    solve(nl)
                    gs = sus[:-1]

            return

        # Find the previous number stored in arr[].
        # It helps in maintaining increasing order
        prev = 1 if(index == 0) else arr[index - 1]

        # note loop starts from previous
        # number i.e. at array location
        # index - 1
        for k in range(prev, num + 1):

            # next element of array is k
            arr[index] = k

            # call recursively with
            # reduced number
            findCombinationsUtil(arr, index + 1, num,
                                 reducedNum - k)

    # Function to find out all
    # combinations of positive numbers
    # that add upto given number.
    # It uses findCombinationsUtil()

    def findCombinations(n):

        # array to store the combinations
        # It can contain max n elements
        arr = [0] * n

        # find all combinations
        findCombinationsUtil(arr, 0, n, n)

    # Driver code
    n2 = n
    k2 = k
    p2 = p
    findCombinations(p2)
    z = z+1
    print("Case #"+str(z)+": " + str(max(sus)))
